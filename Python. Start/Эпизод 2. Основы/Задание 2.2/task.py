from math import *

# Пример 1
def task_1(A):
    res=0
    for i in A:
        if (i>0):
            res+=i
    return res


# Пример 2
def task_2(A):
    res = 0
    for i in A:
        res += i
    return res / len(A)


# Пример 3
def task_3(A):
    mean = sum(A) / len(A)
    squared_diff = [(x - mean) ** 2 for x in A]
    mean_squared_diff = sum(squared_diff) / len(A)
    std_dev = sqrt(mean_squared_diff)
    return std_dev
