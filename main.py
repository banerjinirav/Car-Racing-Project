from random import randint, choice
from time import sleep
from sys import stdout
from os import system
from Cars import Car
from Track import Track

def animate(text, speed=.0325,newLine=True):
  for letter in text:
    stdout.write(letter)
    stdout.flush()
    sleep(speed)
  if newLine:
    stdout.write("\n")
    stdout.flush()

def race(carsList,track):
  print("Here is the lane order:")
  for i,j in enumerate(carsList,1):
    print(i,f"{j.name} with a topspeed of {j.topspeed}")
  raceWon = False
  while not raceWon:
    for j,i in enumerate(carsList):
      if i.speed + i.acceleration > i.topspeed:
        i.speed = i.topspeed
      elif i.speed < i.topspeed:
        i.speed += i.acceleration
        i.randomizeAcceleration()
      move_amount = int(i.speed/track.interval)
      won = track.advanceCar(j,move_amount)
      
      sleep(1)
      system('clear')
      print(track)
      
      if won:
        raceWon = True
        i.updateWins()
        print(f"The winner is {i.name} with {i.wins} wins")
        updateFile("cars.txt",cars)
        track.resetTrack()
        break
      
      

def addCarsFromFile(filename):
  file = open(filename)
  cars = []
  for i in file:
    car = i.split(", ")
    cars.append(Car(car[0],int(car[1]),int(car[2]),int(car[3]),int(car[4])))
  return cars

def updateFile(filename,cars):
  file = open(filename,"w")
  for i in cars:
    file.write(f"{i.name}, {i.topspeed}, {i.minAcc}, {i.maxAcc}, {i.wins}\n")
  
cars = addCarsFromFile("cars.txt")
for i in cars:
  print(i.name)

track = Track(cars,6,10)

for i in range(50):

  race(cars,track)


