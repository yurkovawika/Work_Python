#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
number = int(input("Введите число от 1 до 7: "))
if number == 6 or number == 7:
    print("Да, это выходной")
elif number < 6 and number > 0:
    print("Это не выходной")
else:
    print("Вы ввели некорректное число")
