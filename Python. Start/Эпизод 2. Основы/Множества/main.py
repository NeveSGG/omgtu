cars = ['BMW', 'Audi', 'Kia', 'Honda', 'BMW']
print(cars)
cars = set(cars)
print(cars)
print(type(cars))

# Добавление элемента
cars.add('Volvo')
print(cars)

# Удаление элемента
cars.remove('BMW')
print(cars)

# Длина множества
print(len(cars))

# Оператор in
print('Honda' in cars)

new_cars = {'Dodge', 'Hyundai', 'Volvo', 'Kia'}

# Объединение
print(cars | new_cars)

# Пересечение
print(cars & new_cars)

# Разность
print(cars - new_cars)
