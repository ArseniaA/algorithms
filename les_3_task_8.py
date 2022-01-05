a = []
for i in range(5):
    b = []
    s = 0
    print(f'{i+1}-ая строка')
    for j in range(3):
        n = int(input(f'Введите элемент: '))
        s += n
        b.append(n)
    b.append(s)
    a.append(b)

for i in a:
    print(i)