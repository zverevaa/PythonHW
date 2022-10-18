# coding: cp1251

# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]

n = int(input())
arr = list(range(-n, n + 1))


def MoveArray(num, arr):
    for i in range(num):
        temp = arr[len(arr) - 1]
        for i in reversed(range(len(arr) - 1)):
            arr[i + 1] = arr[i]
        arr[0] = temp
    return arr


print(arr)
print(MoveArray(2, arr))
