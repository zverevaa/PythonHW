# coding: cp1251

# ������ 1. �������� ���������, ������� ��������� �� ���� ����� N � ������ ������ ����������� ��� ����� �� 1 �� N.
# N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

num = int(input())
factorial = 1
arr = []

for i in range(1, num + 1):
    factorial *= i
    arr.append(factorial)

print(arr)
