# Пример цикла while

num = 0
n = int(input('Введите n '))
while num <= n:
    print(num)
    num = num + 1
print("--------")

# пример работы оператора break
num = 0
n = int(input('Введите n '))
while num <= n:
    print(num)
    if num == 10:
        break
    num = num + 1  # данную строчку можно изменить на num+=1

# пример работы оператора continue

num = 0
n = int(input('Введите n '))

while num <= n:
    if num % 2 == 0:
        num += 1
        continue
    print(num)
    num += 1
