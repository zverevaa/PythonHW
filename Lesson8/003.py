# Задача 3. В двумерном массиве хранятся средние дневные температуры с мая по сентябрь за прошлый год. Каждому месяцу соответствует своя строка. Определите самый жаркий и самый холодный 7-дневный промежуток этого периода. Выведите его даты.
import random
from datetime import datetime, timedelta

temperatures = [0] * 5
temp = []
temp_sum = 0
temp_span_max = 0
temp_span_min = 999
months = ['may', 'june', 'july', 'august', 'september']
days = 31

for month in range(len(months)):
    if month == 1 or month == 4:
        days = 30
    temperatures[month] = list(random.randint(15, 30) for _ in range(days))

for row in temperatures:
    print(row)
for i in range(len(temperatures)):
    for j in range(len(temperatures[i])):
        temp.append(temperatures[i][j])
for i in range(len(temp) - 6):
    temp_sum = 0
    for j in range(7):
        temp_sum += temp[i+j]
    if temp_sum > temp_span_max:
        temp_span_max = i
    elif temp_sum < temp_span_min:
        temp_span_min = i

start_date = '2021-05-01'
dt = datetime.strptime(start_date, '%Y-%m-%d')
max_temp_span_start = (
    dt + timedelta(days=temp_span_max)).strftime('%Y-%m-%d')
max_temp_span_finish = (
    dt + timedelta(days=temp_span_max+7)).strftime('%Y-%m-%d')
min_temp_span_start = (
    dt + timedelta(days=temp_span_min)).strftime('%Y-%m-%d')
min_temp_span_finish = (
    dt + timedelta(days=temp_span_min+7)).strftime('%Y-%m-%d')

print(
    f"Самый тёплый промежуток: с {max_temp_span_start} по {max_temp_span_finish}")
print(
    f"Самый холодный промежуток: с {min_temp_span_start} по {min_temp_span_finish}")
