# Напишите программу, которая
# найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

from random import randint
from math import ceil

while True:
    try:
        n = int(input('Введите количество элементов списка: '))
        if n > 0:
            break
    except:
        print('Введите целое число!')

my_list = []

for i in range(n):
    my_list.append(randint(1, 9))

res_list = []
for i in range(int(ceil(len(my_list)/2))):
    item = my_list[i]*my_list[len(my_list) - i - 1]
    res_list.append(item)

print(f'{my_list} -> {res_list}')