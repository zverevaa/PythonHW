# Задача 2. В файле находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва.

data = open('fruits.txt', 'r', encoding="utf-8")

fruits = []

for line in data:
    fruits.append(line)

data.close()

letter = input('Для поиска введите первую букву: ')


def filter_dictionary(letter, arr):
    filtered_fruits = []
    for i in range(len(arr)):
        if (arr[i][0].lower() == letter.lower()):
            filtered_fruits.append(arr[i][:-1])

    if len(filtered_fruits) == 0:
        error = "Нет таких фруктов, попробуйте еще раз"
        return error

    return filtered_fruits


print(f'Фрукты, которые начинаются на букву {letter}:')
print(filter_dictionary(letter, fruits))
