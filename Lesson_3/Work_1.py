# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


my_list = [1, 2, 3, -5, 10, -1.5]
sum = 0
for i in range(1, len(my_list),2):
    #print(my_list[i]) #числа на нечетных позициях
    sum = sum + my_list[i]
print(f"Сумма элементов списка, стоящих на нечётной позиции = {sum}")