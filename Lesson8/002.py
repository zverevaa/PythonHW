# Задача 2. Дана квадратная матрица, заполненная случайными числами. Определите, сумма элементов каких строк превосходит сумму главной диагонали матрицы.

import random

rows = 5
columns = 5
numbers = [0] * rows
diagonalSum = 0
rowSum = 0
rowSumList = []

for i in range(len(numbers)):
    numbers[i] = list(random.randint(1, 9) for _ in range(columns))

for row in numbers:
    print(row)

for i in range(rows):
    rowSum = 0
    for j in range(columns):
        if (i == j):
            diagonalSum += numbers[i][j]
        rowSum += numbers[i][j]
    rowSumList.append(rowSum)


for i, sum in enumerate(rowSumList):
    if (sum > diagonalSum):
        print(
            f'Сумма строки с индексом {i} ({sum}) больше суммы главной диагонали матрицы ({diagonalSum})')

print(rowSumList)
