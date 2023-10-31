#acceleration = changeinspeed/changeintime

def newinput(text):
    value = input(text)
    while value == "" or value.isnumeric() == False:
      if value == "":
         print("Value cannot be empty")
      elif value.isnumeric() == False:
         print("Value must be a number")
      value = input(text)
    return value

speed = newinput("Change in Speed: ")
time = newinput("Change in Time: ")
acc = speed/time
print(f"Acceleration: {acc}m/s/s (ms^-2)")