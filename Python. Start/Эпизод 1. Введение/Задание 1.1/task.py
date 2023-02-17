import math

# Пример 1
def task_1(a, d, c):
    return (c - (d/5) + math.sqrt(321)) / (1 + a * 3)


# Пример 2
def task_2(a, d, c):
    return (math.log(c/3, 10)-d+25)/(a*5-1)


# Пример 3
def task_3(a, d, c):
    return (c/2+math.log(d)-35)/(a*5+1)


# Пример 4
def task_4(a, d, c):
    return (math.tan(c)+(d/32))/(a/3+1)


# Пример 5
def task_5(a, d, c):
    return ((c/5)-d+1)/(c+math.tan(2*a))


# Пример 6
def task_6(a, d, c):
    return (math.sqrt(25*c)+d-3)/(d-a*a+1)


# Пример 7
def task_7(a, d, c):
    return (5*math.log(c, 10)+3*d-32)/(a*a+1)


# Пример 8
def task_8(a, d, c):
    return (c*d - math.log(4*3*a))/(c+a-1)
