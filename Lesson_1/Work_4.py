#Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y)

quarter_number = int(input("Введите номер четверти от 1 до 4 >>  "))
while quarter_number < 1 or quarter_number > 4:
    print("Вы ввели неверное число.")
    quarter_number = int(input("Введите номер четверти от 1 до 4 "))
if quarter_number == 1:
    print ("В этой области  точки X и Y могут принмать занчения от 0 до +∞ ")
elif quarter_number == 2:
    print ("В этой области  точка X может принимать значения от 0 до - ∞,а  точка Y может принмать занчения от 0 до +∞")
elif quarter_number == 3:
    print ("В этой области точка X может принимать значения от 0 до -∞,а точка Y может принмать занчения от 0 до -∞")
elif quarter_number == 4:
    print ("В этой области точка X может принимать значения от 0 до +∞,а точка Y может принмать занчения от 0 до -∞")