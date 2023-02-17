def task_1(lst):
    # Создаем словарь для подсчета частоты каждого числа в списке
    freq = {}

    # Проходимся по каждому элементу в списке и обновляем словарь с его частотой
    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Находим число с максимальной частотой в словаре
    most_common_num = max(freq, key=freq.get)

    # Возвращаем это число
    return most_common_num

def task_2(X, Y):
    for i in range(8):
        for j in range(i+1, 8):
            # Проверяем, находятся ли два ферзя на одной вертикали, горизонтали или диагонали
            if X[i] == X[j] or Y[i] == Y[j] or abs(X[i] - X[j]) == abs(Y[i] - Y[j]):
                return "YES"  # Если ферзи бьют друг друга, возвращаем "YES"
    return "NO"  # Если ферзи не бьют друг друга, возвращаем "NO"

def task_3(x, y, xc, yc, r):
    # Вычисляем расстояние между центром круга и точкой
    distance = ((x - xc)**2 + (y - yc)**2)**0.5

    # Если расстояние меньше или равно радиусу круга, то точка принадлежит кругу
    if distance <= r:
        return True
    else:
        return False

def task_4(lst):
    count = 0
    for i in range(1, len(lst)-1):
        if lst[i] > lst[i-1] and lst[i] > lst[i+1]:
            count += 1
    return count

def task_5(key):
    with open('file.txt', 'r') as f:
        text = f.read()
    encrypted_lines = []
    for line in text.split('\n'):
        encrypted_line = ''
        for char in line:
            if char.isalpha():
                shifted_char = chr((ord(char) - ord('a') + key) % 26 + ord('a'))
                encrypted_line += shifted_char
            else:
                encrypted_line += char
        encrypted_lines.append(encrypted_line)
    return encrypted_lines





