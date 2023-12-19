import math
print("Standard deviation frequency calculator v0.0.0.0.0.0.0.1")
data = {}

def newinput(text, allownothing = False):
    value = input(text)
    if allownothing == True and value =="": return value
    while value == "" or value.replace(".","").isnumeric() == False:
      if value == "":
         print("Value cannot be empty")
      elif value.isnumeric() == False:
         print("Value must be a number")
      value = input(text)
    return value

print("type nothing when done")
while True:
    newdata = newinput("Add new score: ",True)
    if newdata == "":
        break
    else: 
        data[str(newdata)] = float(newinput(f"Set frequency for {newdata}: "))
print(data)


totalfrequecyofvalue = mean = 0
total = 0
for num in data:
    total += data[num]
    totalfrequecyofvalue += data[num]
    mean += data[num] * float(num)
mean = mean/total

result = 0
for num in data:
    result += data[num]*(float(num)-mean)**2

sample= math.sqrt(result/(totalfrequecyofvalue-1))
pop = math.sqrt(result/totalfrequecyofvalue)

try:
  print("Mean: ",round(mean,3),"\nfinal answer model:population =", round(pop,3), f"(Variance: {round(pop**2,3)})")
  print("final answer model:sample =", round(sample,3),f"(Variance: {round(sample**2,3)})")
  #print(result)
except:
  print("errors frfr")