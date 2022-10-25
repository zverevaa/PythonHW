from math import sqrt
# Задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 60 -> 2, 2, 3, 5
user_input = int(input())


def find_prime_factors(num):
    i = 2
    prime_factors = []
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            prime_factors.append(i)
    if num > 1:
        prime_factors.append(num)
    return prime_factors


print(find_prime_factors(user_input))
