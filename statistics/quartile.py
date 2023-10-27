import math

def quartile(list):
  length = len(list)
  for data in range(0, length):
    list[data] = float(list[data])
  list.sort()
  if length % 2 == 0:
    print("even idfk")
  else:
    print(list, length//2)
    return list[length//2]
population = input("Interquartile something calculator v0.0.0.0.0.0.0.1\nData: ").split()
size = len(population)
for data in range(0, size):
  population[data] = float(population[data])
population.sort()
print(population)
if size % 2 == 0:
  print("lol")
else:
  lowerquartile = ""
  upperquartile = ""
  size -= 1
  halfsize = size/2
  median = population[int(halfsize)]
  for x in range(0, int(halfsize)):
    print(x, population[x])
    lowerquartile += f"{population[x]} "
  for x in range(1, int(halfsize+1)):
    upperquartile += f"{population[-x]} "
  print("The median is:",median)
  q1 = quartile(lowerquartile.split())
  q3 = quartile(upperquartile.split())
  print("Lower quartile:",lowerquartile, q1)
  print("Upper quartile:",upperquartile, q3)
  print("IQR: ", q3 - q1)
