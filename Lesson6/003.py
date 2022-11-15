# Задача 3. Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.
import math

div = 11
for i in range(2, div + 1):
    for j in range(1, i):
        if math.gcd(i, j) == 1:
            print(f'{j}/{i}')
