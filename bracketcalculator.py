print("real calculator:\nSupporter operators: +, -, /, *, ^")
equation = initequity = "(" + input("Equation: ") + ")"
print(equation)
operators = ["*","/","-","+","^"]
def operation(initial, value, type):
    value=float(value)
    '''if type == "+":
        return initial+value
    elif type == "-":
        return initial-value
    elif type == "/":
        return initial/value
    elif type == "*":
        return initial*value
    else: return "ERROR3"'''
    match type:
        case "+":
            return initial+value
        case "-":
            return initial-value
        case "/":
            return round(initial/value, 2)
        case "*":
            return initial*value
        case "^":
            return initial**value
        case _:
            return "ERROR3"

def calculate(aequation):
    print(aequation)
    if len(aequation) <= 1:
        return aequation
    result = 0
    loop = 0
    if "(" in aequation:
        aequation = swapbracket(aequation)
        #print("swapping frfr")
    if isinstance(aequation, str):
        aequation = aequation.split()
    while True:
        loop +=1
        if loop > 100:
            return "Critical system error: loop fail"
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
    return aequation

def swapbracket(question):
    bracket = ""
    abracket = 0
    question = "".join(question)
    hasop = False
    negative = False
    for a in question:
        if a == "(":
            if abracket > 0:
                bracket += f" {a} "
            abracket += 1
            continue
        elif a == ")":
            abracket -= 1
            if abracket > 0:
                bracket += f" {a} "
            if abracket == 0:
                print(bracket,bracket.split())
                answer = str("".join(calculate(bracket.split())))
                question = question.replace(f"({"".join(bracket.split())})", answer)
                #print("New question:", question)
            continue
        elif abracket > 0:
            #adds operators
            if a in operators:
                #pls fix this idfk
                if hasop == True and a == "-":
                    hasop = False
                    negative = True
                    continue
                elif hasop == False:
                        hasop = True
                bracket += f" {a} "
                continue
            elif negative == True:
                    negative = False
                    bracket += f" -{a} "
                    print("negative")
                    continue 
            hasop = False
            bracket += a
    if abracket > 0:
        print("Error close bracket when?")
        return "error"
    #print(question)
    return question

while "(" in equation:
        equation = swapbracket(equation)
#print("After brackets", equation)
#print("E finalz")

#final answer frfr
final = ""
x = ""
for everything in "".join(equation):
    #print(everything)
    if everything in operators:
        final+= f" {everything} "
    else: final += everything
    x = everything
#print(final, "FINAL")
answer="".join(calculate(final.split()))
print(initequity,"=", str(answer))