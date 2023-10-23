import math
population = input("Median calculator v0.0.0.0.0.0.0.1\nData: ").split()
size = len(population)
for data in range(0, len(population)):
  population[data] = int(population[data])
population.sort()
print(population)
lowerquartile = size/4
upperquartile = lowerquartile*3
print("Lower quartile:",population[math.floor(lowerquartile)])
if size % 2 != 0:
  print("The median is: ",population[int(size/2)])
else: 
  median = int(size/2)
  x = int(population[median])
  y = int(population[median-1])
  print("The median is:",(x+y)/2)
print("Upper quartile:", population[math.floor(upperquartile)])