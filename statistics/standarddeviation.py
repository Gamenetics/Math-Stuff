import math
population = input("Standard deviation calculator v0.0.0.0.0.0.0.1\nData: ").replace(",","").split()
size = len(population)
for data in range(0, len(population)):
  population[data] = float(population[data])
population.sort()
mean = 0
for num in population:
    mean += float(num)
mean/=size
result = 0
for num in population:
    result += (float(num)-mean)**2
#print(result2)
sample= math.sqrt(result/(size-1))
pop = math.sqrt(result/size)
print("Mean:",mean,"\nStandard Deviation model:sample =",round(sample,3),f"(Variance: {round(sample**2,3)})\n" )
print("Standard Deviation model:population =", round(pop,3), f"(Variance: {round(pop**2,3)})")