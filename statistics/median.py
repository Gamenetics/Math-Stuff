population = input("Median calculator v0.0.0.0.0.0.0.1\nData: ").replace(",","").split()
size = len(population)
for data in range(0, len(population)):
  population[data] = float(population[data])
population.sort()
print(population)
if size % 2 != 0:
  print("The median is: ",population[int(size/2)])
else: 
  median = float(size/2)
  x = float(population[median])
  y = float(population[median-1])
  print("The median is:",(x+y)/2)