#3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

r = [int(el) for el in input().split()]

max = r[0]
min = r[0]

for el in r:
    if el > max:
        max = el
    elif el < min:
        min = el

min_index = r.index(min)
max_index = r.index(max)
r[min_index], r[max_index] = r[max_index], r[min_index]
print(r)