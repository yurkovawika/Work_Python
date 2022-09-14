# 1.Вычислить число c заданной точностью d
# Пример: при $d = 0.001, π = 3.141
# import math
# num = float(input("Введите число num: "))
# d = int(input("Введите число d: "))
# print(round(num, d))


# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]
# N = int(input("Введите число num: "))
# list_N = []
# while N%2 == 0:
#     list_N.append(2)
#     N = N/2
# while N%3 == 0:
#     list_N.append(3)
#     N=N/3
# while N%5 == 0:
#     list_N.append(5)
#     N=N/5
# while N%7 == 0:
#     list_N.append(7)
#     N=N/7
# if N>1:
#     list_N.append(int(N))
# print(list_N)


# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]
# numbers_list = [0,1,1,2,3,3,4,8,4]  #[0,2,8]
# new_list = []
# for i in numbers_list:
#     count = 0
#     for j in numbers_list:
#         if i == j:
#             count +=1
#     if count == 1:
#         new_list.append(i)
# print(new_list)


# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# def polynom(k):
#     import random
#     list = []
#     c = random.randint(0, 100)
#     for i in range(k, 0, -1):
#         if i > 1 and k > 0:
#             a = random.randint(0, 100)
#             list.append(f'{a}*x**{i} + ')
#         elif i == 1:
#             b = random.randint(0, 100)
#             list.append(f'{b}*x + {c} = 0')
#         else:
#             list.append(f'+ {c} = 0 ')
#     if k == 0:
#         list.append(f'{c}')
#     return list
# k = int(input("Введите натуральную степень k: "))
# with open('file.txt', 'w') as f:
#     f.writelines(polynom(k))



# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# with open('file1.txt', 'w') as f: 
#      f.writelines(polynom(2)) # чтобы сработало нужно ракоментить функцию из предыдущего задания
# with open('file2.txt', 'w') as f:
#      f.writelines(polynom(3))

# stroka = []
# with open('file1.txt', 'r') as f1:
#      file1 = 'file1.txt'
#      sum = open(file1, 'r')
#      for line in sum:
#         stroka.append(f'{line[0:-3]}+ ')
# with open('file2.txt', 'r') as f2:
#      file2 = 'file2.txt'
#      sum = open(file2, 'r')
#      for line in sum:
#         stroka.append(f'{line[0:-3]}= 0')
# with open("sum.txt", "w") as s:
#     s.writelines(stroka)




