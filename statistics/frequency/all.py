import math
data = {}

print("frequency full calcualtor frfr")

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
    newdata = input("Add new score: ")
    if newdata == "":
        break
    else: 
        data[int(newdata)] = int(newinput(f"Set frequency for {newdata}: "))

frequecyofvalue = mean = total = 0
for num in data:
    total += data[num]
    frequecyofvalue += data[num] * num
    mean += data[num]

mode = []
for num in data: 
  if data[num] == data[max(data, key=data.get)]:
     mode.append(num)
print("Mean: ",frequecyofvalue/mean)
print("Mode:", mode)

'''
size = len(data)
population.sort()
mean = 0
for num in population:
  mean += int(num)
mean/=size
result = 0
for num in population:
  result += (int(num)-mean)**2

print("Mean: ",mean,"\nfinal answer model:sample =", math.sqrt(result/(size-1)), "\n")

print("final answer model:population =", math.sqrt(result/size))
'''

datalist = []
for num in data:
   for x in range(0,data[num]):
    datalist.append(num)
#print(datalist)
datalist.sort()
size = len(datalist)
if size % 2 != 0:
  print("The median is: ",datalist[int(size/2)])
else: 
  median = int(size/2)
  x = int(datalist[median])
  y = int(datalist[median-1])
  print("The median is: ",(x+y)/2)

cumulativepercentage = 0
print("Total:",total,"\n\n")
for num in sorted(data.items(), key=lambda x:x[1]):
  percent = round((num[1]/total)*100, 1)
  cumulativepercentage += percent
  print(f"Percentage of {num[0]} [{num[1]}/{total}] {percent}% || Cumulative: {cumulativepercentage}%")