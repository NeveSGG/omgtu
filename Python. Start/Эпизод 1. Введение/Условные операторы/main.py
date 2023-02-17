# Игра угадай число
num = 17
value = int(input("Введите число от 1 до 100"))

if value == num:
    print("Поздравляю, вы угадали!!!")
else:
    if value > num:
        print("Введите число меньше")
    else:
        print("Введите число больше")
