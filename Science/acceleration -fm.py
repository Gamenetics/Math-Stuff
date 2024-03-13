#A = F/M

def newinput(text):
    value = input(text)
    while value == "" or value.isnumeric() == False:
      if value == "":
         print("Value cannot be empty")
      elif value.isnumeric() == False:
         print("Value must be a number")
      value = input(text)
    return value

force = newinput("force: ")
mass = newinput("Mass: ")
acceleration = force/mass
print(f"Acceleration: {force}m/s/s (ms^-2)")