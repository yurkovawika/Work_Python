# №1
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# lis = 'Каждый абвпират иабв охотник желает неабвьт знать где сидит синийабв фазан'
# list1 = lis.split()
# def f(i):
#     if "абв" not in i:
#         return i
# m = list(filter(f,list1))
# print(m)

# №2
# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# 1) Игра человек против человека
# bonbon = 2021
# count = 0
# while bonbon > 0:
#     for i in range(1,3):
#         print(f'Cейчас {bonbon} конфет')
#         if bonbon <=28:
#             num = bonbon
#         else:
#             while (num:= int(input(f"Игрок №{i}, возьмите конфеты от 1 до 28 ->> "))) > 28:
#                 print(f'Столько брать нельзя.')
#                 count +=1
#                 if count > 5:
#                     print(f'Играем по правилам!')

#         print(f'Игрок №{i} взял {num} bonbon')
#         bonbon -= num
#         if bonbon == 0:
#             print(f'Выиграл игрок №{i}, взяв {num} bonbon')
#             break

# a) Игра против бота
# import random
# bonbon = 2021
# count = 0
# gamers = ['Bot']
# gamers.append(input("Введите имя игрока: "))
# while bonbon > 0:
#     for i in gamers:
#         print(f'Осталось {bonbon} конфет')
#         if bonbon <=28:
#             num = bonbon
#         else:
#             if i == gamers[1]:
#                 while (num:= int(input(f"{i}, возьми конфет от 1 до 28 ->> "))) > 28:
#                     print(f'Столько брать нельзя.')
#                     count +=1
#                     if count > 5:
#                         print(f'Играем по правилам!')
#             elif i == gamers[0]:
#                 num = random.randint(1,28)
#                 print(f'{i} взял {num} конфет')
#         # print(f'{i} взял(а) {num} bonbon')
#         bonbon -= num
#         if bonbon == 0:
#             print(f'Выиграл игрок {i}, взяв {num} конфет')
#             break

# b) Подумайте как наделить бота ""интеллектом""
# import random
# bonbon = 2021
# step = random.randint(0,1)
# gamers2 = (input("Введите имя игрока: "))
# if step == 0:
#     gamers = ['Bot', gamers2]
#     print(f'По результатам жеребьевки первым ходит игрок Bot')
# elif step == 1:
#     gamers = [gamers2,'Bot']
#     print(f'Первым ходит игрок {gamers2}')

# while bonbon > 0:
#     for i in gamers:
#         print(f'Осталось {bonbon} конфет')
#         if i == gamers2:
#             while (num:= int(input(f"{i}, возьми конфет от 1 до 28 ->> "))) not in range(1,29):
#                 if num == 0:
#                     print(f'Вы взяли 0 конфет, возьмите больше.')
#                 else:
#                     print(f'Столько брать нельзя.')
#         else:
#             if bonbon <=28:
#                 num = bonbon
#             else:
#                 num = random.randint(1,28)
#                 print(f'{i} взял {num} конфет')
#         bonbon -= num
#         if bonbon == 0:
#             print(f'Выиграл игрок {i}, взяв {num} конфет')
#             break


# №4
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


# f = open('text.txt', 'r')
# strok = f.read()
# zip =''
# char= ''
# count=1
# for i in range(1,len(strok)):
#     if strok[i] == strok[i-1]:
#         count +=1

#     else:
#         if count > 1:
#             zip += str(count)+strok[i-1]
#         else:
#             zip += strok[i-1]
#         count=1

#     if i == len(strok) - 1:
#         if count > 1:
#             zip += str(count)+strok[i]
#         else:
#             zip += strok[i]
# data = open('zip.txt', 'w')
# data.writelines(zip)
# data.close()


# data = open('zip.txt', 'w')
# data.writelines(zip)
# data.close()

# numbers = [str(i) for i in range (0,10)]
# unzip = ''
# a = ''
# for i in range(0,len(zip)):
#     if zip[i] in numbers:
#         a += str(zip[i])
#     else:
#         if a != '':
#             unzip += ((int(a)-1)*zip[i])
#         unzip += zip[i]
#         a = ''

# unzip_text = open('unzip.txt', 'w')
# unzip_text.writelines(unzip)
# unzip_text.close()
# f.close()