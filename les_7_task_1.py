# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком. Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

def bubble_sort(array):
    array = [randint(-100, 100) for i in range(int(input()))]
    print(array)

    n = 1
    while n < len(array):
        for i in range(len(array) - n):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1

    print(array)

bubble_sort(a)


def bubble_sort1(array):
    array = [randint(-100, 100) for i in range(int(input()))]
    print(array)

    for j in range(len(array) - 1):
        for i in range(len(array) - 1 - j):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]

    print(array)

bubble_sort1(a)