#Напишите программу, которая будет преобразовывать десятичное число в двоичное.

num = int(input("Введите число: "))
bin= " "
while num > 0:
    i = num%2
    bin  = str(i) + bin
    num = num //2
print(bin)


