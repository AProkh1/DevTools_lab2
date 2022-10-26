def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

otv = int(input('1.plus or 2.minus'))
n1 = int(input('Write a first number'))
n2 = int(input('Write a second number'))

if otv == 1:
    print(plus(n1,n2))
if otv == 2:
    print(minus(n1,n2))
