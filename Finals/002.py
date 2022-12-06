# Задача 2. Имеются данные о площади и стоимости 15 домов.
# Риелтору требуется узнать в каких домах стоимость квадратного метра меньше 50000 рублей.
# Предоставьте ему графические данные о стоимости квадратного метра каждого дома и список подходящих ему домов, отсортированных по площади.
# Данные о домах сформируйте случайным образом. Площади от 100 до 300 кв. метров, цены от 3 до 20 млн.
from random import randint
import matplotlib.pyplot as plt
x = []
house_amount = 15

house_sq = [randint(100, 300) for i in range(house_amount)]
house_price = [randint(3000000, 20000000) for i in range(house_amount)]
sq_price = []
for i in range(house_amount):
    sq_price.append(int(house_price[i] / house_sq[i]))

for i in range(0, house_amount):
    x.append(i+1)
x_plot = x


def sortArray(arr, i, j):
    temp = 0
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def sortArrays(main_arr, second_arr, x):
    for i in range(len(main_arr) - 1):
        for j in range(i+1, len(main_arr)):
            if main_arr[j] > main_arr[i]:
                sortArray(main_arr, i, j)
                sortArray(second_arr, i, j)
                sortArray(x, i, j)


sortArrays(house_sq, house_price, x)

print('Подходящие дома по стоимости квадратного метра(отсортированы по площади)')
for i in range(house_amount):
    if sq_price[i] <= 50000:
        print(
            f'№ дома {x[i]} Площадь: {house_sq[i]}, цена: {house_price[i]}, цена за кв. метр: {sq_price[i]}')


plt.xlabel('Номер дома')
plt.ylabel('Стоимость квадратного метра')
plt.axhline(y=50000, color='r')
plt.bar(x_plot, sq_price)
plt.show()
