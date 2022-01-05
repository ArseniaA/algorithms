a = [int(el) for el in input().split()]

max = a[0]
min = a[-1]

for i in range(len(a)):
    if a[i] > max:
        max = a[i]
        max_index = i
    elif a[i] < min:
        min = a[i]
        min_index = i

if min_index > max_index:
    min_index, max_index = max_index, min_index

sum = 0
for j in range(min_index+1, max_index):
    sum += a[j]
print(sum)