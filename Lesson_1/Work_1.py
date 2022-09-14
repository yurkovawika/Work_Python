# #Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# number = int(input("Введите число от 1 до 7: "))
# if number == 6 or number == 7:
#     print("Да, это выходной")
# elif number < 6 and number > 0:
#     print("Это не выходной")
# else:
#     print("Вы ввели некорректное число")




# color =['red','green','blue']
# data = open('file.txt', 'w')
# data.writelines(color)
# data.write('\nLine2\n')
# data.write('Line3\n')
# data.close()


# color =['red','green','blue']
# for i in color:
#     with open('file.txt','a') as data:
#         data.write(F'{i}\n')

path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()

exit()