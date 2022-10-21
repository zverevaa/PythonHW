# Задача 1. Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8

num = int(input('Введите число: '))


def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)


for e in range(1, num + 1):
    data = open('fibonacci.txt', 'a')
    data.writelines(f'{str(fib(e))} ')

data.close()
