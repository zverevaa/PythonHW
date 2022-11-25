# Задача 3. В двумерном массиве хранятся средние дневные температуры с мая по сентябрь за прошлый год. Каждому месяцу соответствует своя строка. Определите самый жаркий и самый холодный 7-дневный промежуток этого периода. Выведите его даты.
import random

months = 5
temps = [0] * months
days = 31

maxTemp = 0
maxTempIndex = 0
minTemp = 0
minTempIndex = 0

daysSpan = 7

for month in range(months):
    if month == 1 or month == 4:
        days = 30
    temps[month] = list(random.randint(15, 30) for _ in range(days))

for i in temps:
    print(i)

tempsFull = []
for temp in temps:
    for i in temp:
        tempsFull.append(i)
print(tempsFull)

tempsSums = []
for i in range(len(tempsFull) - daysSpan + 1):
    tempsSums.append(sum(tempsFull[i:i+daysSpan]))

print(tempsSums)

maxTemp = max(tempsSums)
maxTempIndex = tempsSums.index(maxTemp)
print(maxTemp)
print(maxTempIndex)


start_x = 0
start_y = 0

for index_x in range(len(temps)):
    if len(temps[index_x]) > maxTempIndex:
        print(f'max el in {temps[index_x]} = {temps[index_x][maxTempIndex]}')
        start_x = index_x
        start_y = maxTempIndex
        break
    else:
        maxTempIndex -= len(tempsFull)

for i in range(daysSpan):
    print(start_x)
    index_y = (start_y + i) % (len(temps[start_x]) + 1)
    length = len(temps[start_x])
    start_x = start_x + (start_y + i) // len(temps[start_x])
    index_y = (start_y + i) % len(temps[start_x])
    print(temps[start_x][index_y], end=' ')
