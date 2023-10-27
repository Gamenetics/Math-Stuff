import math
print("Standard deviation frequency calculator v0.0.0.0.0.0.0.1")
data = {}

def newinput(text, allownothing = False):
    value = input(text)
    if allownothing == True and value =="": return value
    while value == "" or value.isnumeric() == False:
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
        data[int(newdata)] = int(newinput(f"Set frequency for {newdata}: "))
print(data)


totalfrequecyofvalue = mean = 0
total = 0
for num in data:
    total += data[num]
    totalfrequecyofvalue += data[num]
    mean += data[num] * num

mean = mean/total

result = 0
for num in data:
    result += data[num]*(int(num)-mean)**2
try:
  print("Mean: ",round(mean,3),"\nfinal answer model:sample =", round(math.sqrt(result/(totalfrequecyofvalue-1)),3), "\n")
  #print(result)
  print("final answer model:population =", round(math.sqrt(result/totalfrequecyofvalue),3))
except:
  print("errors frfr")