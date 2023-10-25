import math
population = input("Median calculator v0.0.0.0.0.0.0.1\nData: ").split()
for data in range(0, len(population)):
  population[data] = int(population[data])
size = len(population)
population.sort()
if size % 2 == 0:
  print("lol")
else:
  median = size/2
  lowerquartile = median/2
  upperquartile = median*1.5
  print("Lower quartile:",population[math.floor(lowerquartile)])
  median = int(size/2)
  print("The median is:",population[median])
  print("Upper quartile:", population[math.floor(upperquartile)])