print("Um so like brackets need a operator inside to work idfk")
equation = input("Equation: ")
abracket = 0
bracket = ""
operators = ["*","/","-","+"]
def operation(initial, value, type):
    value=float(value)
    if type == "+":
        return initial+value
    elif type == "-":
        return initial-value
    elif type == "/":
        return initial/value
    elif type == "*":
        return initial*value
    else: return "ERROR3"

def calculate(aequation):
    print(aequation)
    if len(aequation) <= 1:
        return equation
    result = 0
    loop = 0
    while True:
        loop +=1
        print("Loop: ", loop)
        for op in operators:
            if op in aequation:
                order=op
                break
            else: 
                order="done"
        if order == "done":
            break
        type = "no"
        for num in aequation:
            print(aequation)
            print(num, num.strip('-').replace(".","").isnumeric())
            if (num.strip('-').replace(".","")).isnumeric() == True:
                if type == "no":
                    result = float(num)
                    last = num
                    continue
                result = operation(result,num,type)
                for i in range(len(aequation)):
                    if aequation[i+2] == num and aequation[i+1] == type:
                        aequation[i] = str(result)
                        aequation.remove(num)
                        aequation.remove(type)
                        break
                type = "no"
                last = num
                break
            elif num == order:
                type = order
            else:
                type = "no"
    return result
for a in equation:
    if abracket > 0:
        #adds operators
        if a in operators:
            bracket += f" {a} "
            continue
        bracket += a
    if a == "(":
        abracket += 1
        bracket += a
        continue
    elif a == ")":
        abracket -= 1
        if abracket == 0:
            answer = calculate(bracket.replace("(","").replace(")","").split())
            '''for i in range(len(equation)):
                if answer[i] == "(":
                    break'''
            equation = equation.replace(bracket.replace(" ", ""), str(answer))
            bracket = ""
if abracket > 0:
    print("Error close bracket when?")
print("After brackets", equation) #WTF ????? ??/ ??\\
#final answer frfr
final = ""
for everything in equation:
    if everything in operators:
        final+= f" {everything} "
    else: final += everything
print("Final Answer:", calculate(final.split()))