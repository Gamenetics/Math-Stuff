data = {}

print("Table frequency mean calcualtor frfr")

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
print(data)
size = len(data)

totalfrequecyofvalue = mean = 0
for num in data:
    totalfrequecyofvalue += data[num] * num
    mean += data[num]

print("Mean: ",totalfrequecyofvalue/mean)