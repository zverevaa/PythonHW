# coding: cp1251

# ������ 3. �������� ���������, ������� �� ��������� ������ ��������, ���������� �������� ��������� ��������� ����� � ���� �������� (x � y).
# 1 -> x > 0, y > 0

quad = int(input("������� ����� ��������: "))


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
        print("������� ����� �� 1 �� 4")


print_coordinates(quad)
