#F = m * a

def newinput(text):
    value = input(text)
    while value == "" or value.isnumeric() == False:
      if value == "":
         print("Value cannot be empty")
      elif value.isnumeric() == False:
         print("Value must be a number")
      value = input(text)
    return value

mass = newinput("Mass: ")
acceleration = newinput("Acceleration: ")
force = mass * acceleration
print(f"Force: {force}N")