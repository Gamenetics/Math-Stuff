import math
print("Some sort of quadratic equation stuff calcualtor frfr")
print("Format: ax^2+bx+c=0")
equation = input("Equation: ").replace("^2","").replace("+","").replace("-","")

equation = equation.split("x")
if len(equation) > 3: print("Error wrong format frfr")
try: 
   a = float(equation[0])
   b = float(equation[1])
   c = float(equation[-1])
   discriminant = (b)**2-4*(a)*(c)
   if discriminant < 0: print("No real solutions")
   else: 
      print("1 real solutions" if discriminant == 0 else "2 real solutions")
      what = float(math.sqrt(discriminant))
      print("Answers:\n" + f"{(-b+what)/float(2*a)}")
      if discriminant > 0: print((-b-what)/float(2*a))
except: print("error")