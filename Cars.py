from random import randint
class Car:
  def __init__(self,name,topspeed,minAcc,maxAcc,wins=0):
    self.name = name   
    self.topspeed = topspeed
    self.acceleration = randint(minAcc,maxAcc)
    self.speed = 0
    self.distance = 0
    self.wins = wins
    self.minAcc = minAcc
    self.maxAcc = maxAcc

  def updateWins(self):
    self.wins += 1

  def randomizeAcceleration(self):
    self.acceleration = randint(self.minAcc,self.maxAcc)