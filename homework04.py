# Напишите программу, которая будет
# преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

while True:
    try:
        n = int(input('Введите количество элементов списка: '))
        if n > 0:
            break
    except:
        print('Введите целое число!')
