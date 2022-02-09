# На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
n = int(input("Введите количество друзей: "))

g = []
for i in range(n):
    row = [1] * s
    row[i] = 0
    g.append(row)

print(g)

handshakes = 0
for row in graph:
    for i in len(row):
        handshakes += i

handshakes //= 2

print(f"Всего рукопожатий")
