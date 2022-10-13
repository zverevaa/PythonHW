# coding: cp1251

# Задача 3. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# 1 -> x > 0, y > 0

quad = int(input("Введите номер четверти: "))


def print_coordinates(quad):
    if quad == 1:
        print("x > 0; y > 0")
    elif quad == 2:
        print("x < 0; y > 0")
    elif quad == 3:
        print("x < 0; y < 0")
    elif quad == 4:
        print("x > 0; y < 0")
    else:
        print("Введите число от 1 до 4")


print_coordinates(quad)
