# 3. Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

text1 = input("Введите строку 1: ")
text2 = input("Введите строку 2: ")
l=len(text2)
j=0
count = 0
for i in text1:
    if  (text2 in text1):
        count +=1 
          
print(f"Количество вхождений 2ой строки в 1ую = {count}")


