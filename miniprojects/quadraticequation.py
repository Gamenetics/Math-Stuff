import math
print("Some sort of quadratic equation stuff calcualtor frfr")

def newinput(text):
    value = input(text)
    while value == "" or value.replace("-","").isnumeric() == False:
      if value == "":
         print("Value cannot be empty") 
      elif value.isnumeric() == False:
         print("Value must be a number")
      value = input(text)
    return value

    
    
print("Format ax^2+bx+c=0")
a = float(newinput("Value A: "))
b = float(newinput("Value B: "))
c = float(newinput("Value C: "))
discriminant = (b)**2-4*(a)*(c)
print(discriminant)
if discriminant < 0: print("No real solutions")
else: 
  print("1 real solutions" if discriminant == 0 else "2 real solutions")
  what = float(math.sqrt(discriminant))
  print("Answers:\n",(-b+what)/float(2*a))
  if discriminant > 0: print((-b-what)/float(2*a))

