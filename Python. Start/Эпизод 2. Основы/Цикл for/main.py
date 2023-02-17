# работа цикла for с списком
group = ['Sam', 'John', 'Степан']

for man in group:
    print(man)
# работа цикла for с строкой
my_str = "hello"

for letter in my_str:
    print(letter)
# работа цикла for с кортежем
my_tuple = (1, 2, 3, 4)

for element in my_tuple:
    print(element)

my_range = range(1, 10)
print(list(my_range))

for i in range(0, 50, 2):
    print(i)
