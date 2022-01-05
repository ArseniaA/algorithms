array = [int(el) for el in input().split()]
indexes = []

for i in range(len(array)):
    if array[i] % 2 == 0:
        indexes.append(i)

print(indexes)
