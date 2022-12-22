# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

my_list = []
n = 5

for i in range(n):
    my_list.append(randint(1, 9))
print(f'Заданный список: \n{my_list}')

index_list = []
sum = 0
for j in range(1, len(my_list), 2):
    sum += my_list[j]
    index_list.append(my_list[j])
print(f'На нечётных позициях элементы {index_list[0]} и {index_list[1]}, ответ: {sum}')

