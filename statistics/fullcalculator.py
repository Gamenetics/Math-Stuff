import math
population = input("Math Statistics calculator v0.0.0.0.0.0.0.1\nData: ").replace(",","").split()
size = len(population)
for data in range(0, len(population)):
  population[data] = float(population[data])
population.sort()
print("Ordered list: ",population)
numbers = {}
for num in population:
    key = str(num)
    if key in numbers:
       numbers[key] = 1+numbers[key]
    else:
       numbers[key] = 1
mean = 0
for num in population:
    mean += float(num)
mean/=size
result = 0
for num in population:
    result += (float(num)-mean)**2
if size % 2 != 0:
  print("The median is:",population[int(size/2)])
else: 
  median = float(size/2)
  x = float(population[median])
  y = float(population[median-1])
  print("The median is:",(x+y)/2)
mode = ""
for num in numbers: 
  if numbers[num] == numbers[max(numbers, key=numbers.get)]:
     mode += f"{num} "
print("Mode:", mode)
sample= math.sqrt(result/(size-1))
pop = math.sqrt(result/size)
print("Mean:",mean,"\nStandard Deviation model:sample =",round(sample,3),f"(Variance: {round(sample**2,3)})\n" )
print("Standard Deviation model:population =", round(pop,3), f"(Variance: {round(pop**2,3)})")