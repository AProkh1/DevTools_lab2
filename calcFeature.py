def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def umn(a, b):
    return a * b

def deli(a, b):
    return a / b

otv = int(input('1.plus; 2.minus; 3.umb; 4.del?'))
n1 = int(input('Write a first number'))
n2 = int(input('Write a second number'))

if otv == 1:
    print(plus(n1,n2))
if otv == 2:
    print(minus(n1,n2))
if otv == 3:
    print(umn(n1,n2))
if otv == 4:
    print(deli(n1,n2))
else:
    print("You write wrong number"