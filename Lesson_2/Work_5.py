#Реализуйте алгоритм перемешивания списка.
import random
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random_list = []
i = 1
while i <= len(my_list):
    rand = random.randint(my_list[0], my_list[-1])
    if rand not in random_list:
        random_list.append(rand)
        i= i+1
    elif rand in random_list:
        rand = random.randint(my_list[0], my_list[-1])
print(random_list)