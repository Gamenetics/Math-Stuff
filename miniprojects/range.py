population = input("Range calculator v0.0.0.0.0.0.0.1\nData: ").split()
for data in range(0, len(population)):
  population[data] = int(population[data])
population.sort()
range = population[-1] - population[0]
print(population)
print("Range: ",range)