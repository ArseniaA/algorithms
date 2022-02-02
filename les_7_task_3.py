# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).

import random

array = [i for i in range(int(input("Введите размер массива: "))]
random.shuffle(array)
print(array)


def select_median(array):
    if len(array) != 1:
        if len(array) % 2 == 1:
            pivot = random.choice(array)
            lows = [el for el in array if el < pivot]
            highs = [el for el in array if el > pivot]
            pivots = [el for el in array if el == pivot]

            if len(lows) == len(highs):
                return pivot
            else:
                return select_median(array)
    else:
        return array[0]
