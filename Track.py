class Track:

  def __init__(self, cars, distance, interval):
    self.distance = distance
    self.lanes = len(cars)
    self.cars = cars
    self.interval = interval
    self.resetTrack()

  def __str__(self):
    track = ""
    for i in range(self.distance):
      for j in range(self.lanes):
        track += self.track[i][j]
      track += "\n"
    return track

  def advanceCar(self, col, amount):
    won = False
    for i in range(self.distance):
      if self.track[i][col] == "|V|":
        dist = -1
        if i + amount >= self.distance:
          dist = self.distance-1
          won = True
        elif i + amount <= self.distance-1:
          dist = i + amount
        self.track[i][col] = "| |"
        self.track[dist][col] = "|V|"
        return won

  def resetTrack(self):
    self.track = []
    for i in range(self.distance):
        lane = []
        for j in range(self.lanes):
          if i == 0:
            lane.append("|V|")
          else:
            lane.append("| |")
        self.track.append(lane)
    for i in self.cars:
      i.speed = 0