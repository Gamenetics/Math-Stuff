print("Um so like brackets need a operator inside to work idfk")
equation = initequity = input("Equation: ")
operators = ["*","/","-","+"]
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
            return initial/value
        case "*":
            return initial*value
        case _:
            return "ERROR3"

def calculate(aequation):
    print(aequation)
    if len(aequation) <= 1:
        return equation
    print("new",aequation)
    result = 0
    loop = 0
    if "(" in aequation:
        aequation = swapbracket(aequation)
    while True:
        loop +=1
        if loop > 100:
            return "Critical system error"
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
            if (num.strip('-').replace(".","")).isnumeric() == True:
                if type == "no":
                    result = float(num)
                    last = num
                    continue
                result = operation(result,num,type)
                for i in range(len(aequation)):
                    print(aequation)
                    if aequation[i+2] == num and aequation[i+1] == type:
                        aequation[i] = str(result)
                        print(aequation)
                        aequation.remove(num)
                        aequation.remove(type)
                        print(aequation)
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
                print("old question", question)
                if isinstance(question, list):
                    question = "".join(question)
                    print("new question frfr", question)
                answer = str("".join(calculate(bracket.split())))
                print("maincheck:",question, (f"({"".join(bracket.split())})"))
                question = question.replace(f"({"".join(bracket.split())})", answer)
                print("New question:", question)
            continue
        elif abracket > 0:
            #adds operators
            if a in operators:
                bracket += f" {a} "
                continue
            bracket += a
    if abracket > 0:
        print("Error close bracket when?")
        return "error"
    print(question)
    if isinstance(question, str):
        a = ""
        for x in question:
            if x in operators:
                a += f" {x} "
                continue
            a += x 
        question = a.split()
    print(question)
    return question

while "(" in equation:
        equation = swapbracket(equation)
print("After brackets", equation)
print("E finalz")

#final answer frfr
final = ""
for everything in equation:
    if everything in operators:
        final+= f" {everything} "
    else: final += everything
print(final, "FINAL")
print("Question: ",initequity,"\nAnswer:", calculate(final.split()))