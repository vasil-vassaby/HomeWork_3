# Задайте список из вещественных чисел.
# Напишите программу, которая
# найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# my_list = [1.1, 1.2, 3.1, 5, 10.01]

from random import uniform

n = 5

my_list = [round(uniform(1, 10), 2) for elem in range(n)]

new_list = []
for i in range(len(my_list)):
    if type(my_list[i]) != float:
        continue
    else:
        item = round(my_list[i] % 1, 2)
        new_list.append(item)
res = round(max(new_list) - min(new_list), 2)

print(my_list,'->', res)
