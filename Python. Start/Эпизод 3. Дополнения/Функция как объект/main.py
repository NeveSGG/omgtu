def my_func():
    print('Hello world!')


def your_func(f):
    f()


your_func(my_func)


# Фильтрация по четности
def filter(numbers):
    res = []
    for num in numbers:
        if num % 2 == 0:
            res.append(num)
    return res


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Ура! Все работает!', filter(numbers))


# Фильтр по какой либо функции

def big_filter(numbers, func):
    res = []
    for num in numbers:
        if func(num):
            res.append(num)
    return res


# напишем функцию проверки на четность
def is_even(num):
    return num % 2 == 0


print(big_filter(numbers, is_even))


# напишем функцию проверки на нечетность
def is_even(num):
    return num % 2 != 0


print(big_filter(numbers, is_even))
