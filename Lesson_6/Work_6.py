# # № 1 Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# numbers_list = [0,1,1,2,3,3,4,8,4]
# new_list = [i for i in numbers_list if numbers_list.count(i)<2]
# print(new_list)
#

# # № 2 Напишите программу, которая найдёт произведение пар чисел списка.
# # Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# # Пример:- [2, 3, 4, 5, 6] => [12, 15, 16]; - [2, 3, 5, 6] => [12, 15]
#
# import math
# my_list = [2, 3, 4, 5, 6]
# stop = math.ceil(len(my_list)/2)
# j =-1
# sum = [my_list[i]*my_list[j+(i*j)] for i in range(0,stop,1) ]
# print(sum)


# # № 3 Напишите программу, которая принимает на вход цифру,обозначающую день недели, и проверяет, является ли этот день выходным.
# while (num:= int(input("Введите число от 1 до 7: "))) not in range(1,8):
#     print('Вы ввели некоррекное число.')
# t = lambda x: "Выходной"  if x > 5 and  x < 8 else "Не выходной"
# print(t(num))