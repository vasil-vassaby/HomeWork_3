# Задайте число.
# Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# Негафибоначчи

while True:
    try:
        k = int(input('Введите число: '))
        if k > 0:
            break
    except:
        print('Введите целое положительное число!')
def fib(n):
    a, b = 0, 1
    for _ in range(n+1):
        yield a
        a, b = b, a + b
def negafib(n):
    a, b = 1, -1
    for _ in range(n):
        yield a
        a, b = b, a - b

print(list(reversed(list(negafib(k)))) + (list(fib(k))))