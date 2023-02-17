def task_1(lst, x):
    low, high = 0, len(lst) - 1

    while low <= high:
        mid = (low + high) // 2

        if lst[mid] == x:
            return str(mid)
        elif lst[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def task_2(num):
    # Проверяем, что число не меньше 2
    if num < 2:
        return False

    # Перебираем делители от 2 до num // 2 + 1
    for i in range(2, num // 2 + 1):
        # Если число делится без остатка на делитель, оно не является простым
        if num % i == 0:
            return False

    # Если цикл завершился без возврата False, то число является простым
    return True
