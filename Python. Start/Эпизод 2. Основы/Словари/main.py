my_dict = {
    'name': "Alex",
    'age': 27
}
# получение элемента по ключу
print(my_dict['age'])

# добавление значения по ключу
my_dict['hair'] = "Brown"
print(my_dict)

# изменение значения
my_dict['hair'] = "Black"
print(my_dict)

# удаление значения
del my_dict['age']
print(my_dict)

# оператор in
if 'age' in my_dict:
    print(True)

if 'hair' in my_dict:
    print(True)
# Перебор по ключам
for key in my_dict:
    print(key)
# Перебор по значениям
for value in my_dict.values():
    print(value)
# Перебор по парам
for key,value in my_dict.items():
    print(key,value)