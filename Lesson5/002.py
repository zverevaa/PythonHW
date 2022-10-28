# Задача 2. Дан список случайных чисел. Создайте список, в который попадают числа, описывающие возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] =>[1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
import random


numbers = [random.randint(1, 10) for i in range(10)]
print(numbers)

def make_sequence(numbers):
    result = [numbers[0]]
    for number in numbers:
        if number > result[-1]:
            result.append(number)
    return result

print(make_sequence(numbers))