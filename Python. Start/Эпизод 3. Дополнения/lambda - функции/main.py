# Фильтр по какой либо функции

def big_filter(numbers, func):
    res = []
    for num in numbers:
        if func(num):
            res.append(num)
    return res


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('Ура! Все работает!', big_filter(numbers, lambda num: num % 2 == 0))
# напишем для нечетности
print('Ура! Все работает!', big_filter(numbers, lambda num: num % 2 != 0))
# для всех чисел больше 5
print('Ура! Все работает!', big_filter(numbers, lambda num: num > 5))
