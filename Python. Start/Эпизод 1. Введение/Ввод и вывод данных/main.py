# вывод разных типов
first_name = "Саша"
age = 34
print(first_name, age)
# вывод через сепаратор
print(first_name, age, sep='/')
# вывод с концом строки
print(first_name, age, end=';')
print()

print("---------->")
# функция input() без параметра
age = input()
print("Вы ввели", age)
# функция input() с параметром
name = input("Введите ваше имя ")
print("Привет", name)
