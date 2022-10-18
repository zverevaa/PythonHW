# coding: cp1251

# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

from itertools import count

str1 = 'one'
str2 = 'onetwonine'

for i in range(len(str1)):
    print(f'{str1[i]} - {str2.count(str1[i])}')
