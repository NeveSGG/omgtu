# функция без параметра
def my_function1():
    print("Привет, я функция без параметра")


my_function1()


# функция с 1 параметром
def my_function2(age):
    print('Привет я функция с 1 параметром и мне %s лет)))' % age)


my_function2(28)


# функция с 2 параметрами
def my_function3(first_param, second_param):
    print('Привет я функция с 2 параметрами, вот первый {}, а вот второй {}'.format(first_param, second_param))


my_function3(1, 2)


# функция с возвращаемым значением
def my_sum(a, b):
    return a + b


print(my_sum(2, 5))
