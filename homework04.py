# Напишите программу, которая будет
# преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

while True:
    try:
        n = int(input('Введите число: '))
        if n > 0:
            break
    except:
        print('Введите целое число!')

new_list = []

while n > 0:
    item = n % 2
    new_list.append(item)
    n //= 2
print(new_list.reverse())