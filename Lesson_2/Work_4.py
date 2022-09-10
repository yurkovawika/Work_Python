# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.
import random
N = int(input("Введите число: "))
my_list = []
j=0
while j < N:
    my_list.append(random.randint(-N, N))
    j+=1
print(my_list)

mult = 1
num_list = list(map(int, input("Введите список чисел: ").split()))
for i in num_list:
    mult = my_list[i]*mult
print(F"Произведение элементов =  {mult}")