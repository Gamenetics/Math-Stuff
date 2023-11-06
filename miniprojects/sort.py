population = input("Median calculator v0.0.0.0.0.0.0.1\nData: ").replace(",","").split()
size = len(population)
for data in range(0, len(population)):
  population[data] = float(population[data])
population.sort()
print(population)