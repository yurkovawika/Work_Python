# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

list = [1.1, 1.2, 3.1, 5.4 , 10.02]
def max_min(list):
    min = 1
    max = 0
    for i in list:
        if (i - int(i)) <= min:
            min = i - int(i)
        if (i - int(i)) >= max:
            max = i - int(i)
    print(max-min)

max_min(list)