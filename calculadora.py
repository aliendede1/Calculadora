# def

def soma(val1:int, val2:int):
    return (val1+val2)

def sem(val1:int, val2:int):
    return (val1-val2)

def vez(val1:int, val2:int):
    return (val1*val2)

def div(val1:int, val2:int):
    return (val1/val2)


## calculadora

val1 = input("diga um numero =")
val2 = input("diga outro =")
val3 = input("")
soma = soma(int (val1) ,int (val2))
sem = sem(int (val1) ,int (val2))
vez = vez(int (val1), int (val2))
div = div(int (val1), int (val2))

# if

if val3 == "+":
    print(soma)
elif val3 == "-":
    print(sem)
elif val3 == "*":
    print(vez)
elif val3 == "/":
    print(div)
