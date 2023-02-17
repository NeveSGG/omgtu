from math import *

# Пример 1
def task_1(a, b):
    if (a>b):
        print(sqrt(a*b)-3, 1, 'a=', a, 'b=', b)
        return sqrt(a*b)-3
    elif (a==b):
        print(log(2, 10), 1, 'a=', a, 'b=', b)
        return 0.3010299956639812
    else:
        print((log(a**3+1))/b, 1, 'a=', a, 'b=', b)
        return (log(a**3+1))/b


# Пример 2
def task_2(a, b):
    if (a < b):
        return tan(a/b)+1
    elif (a == b):
        print(tan(-1), 2, 'a=', a, 'b=', b)
        return tan(-1)
    else:
        return sqrt(a*b-5)/a


# Пример 3
def task_3(a, b):
    if (a > b):
        return log(a*b, 10)+21
    elif (a == b):
        print(tan(-5), 3, 'a=', a, 'b=', b)
        return tan(-5)
    else:
        return log(3*(a/b))+1


# Пример 4
def task_4(a, b):
    if (a > b):
        return sqrt(a*b-1)
    elif (a == b):
        print(log(255, 10), 4, 'a=', a, 'b=', b)
        return 2.406540180433955
    else:
        return tan(a-5)/b


    # Пример 5
def task_5(a, b):
    if (a > b):
        return log(a/b)+31
    elif (a == b):
        print(tan(-25), 5, 'a=', a, 'b=', b)
        return tan(-25)
    else:
        return cos(a*5-1)/a


    # Пример 6
def task_6(a, b):
    if (a < b):
        return sqrt((b/a)+1)
    elif (a == b):
        print(5, 5, 'a=', a, 'b=', b)
        return 5
    else:
        return log(a**3 - 5, 10)/b
