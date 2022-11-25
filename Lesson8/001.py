# Задача 1. В каждой группе учится от 20 до 30 студентов. По итогам экзамена все оценки заносятся в таблицу. Каждой группе отведена своя строка. Определите группу с наилучшим средним баллом.

import random

rows = 5
columns = random.randint(20, 30)
scores = [0] * rows
calculatedScores = 0
bestGroupIndex = 0
bestGroupScore = 0
groupI = 1


print('\nОбщая таблица средних баллов:\n')

for i in range(len(scores)):
    scores[i] = list(random.randint(2, 5) for _ in range(columns))
    calculatedScores = 0
    for j in range(columns):
        calculatedScores += scores[i][j]
    print(f'Группа {i + 1} : {calculatedScores} ')
    if (bestGroupScore < calculatedScores):
        bestGroupIndex = i
        bestGroupScore = calculatedScores

print('\nОбщая таблица результатов:\n')

for row in scores:
    print(f'Группа {groupI} : {row}')
    groupI += 1


print(
    f'\nПобеждает группа {bestGroupIndex + 1} с результатом {bestGroupScore}')
