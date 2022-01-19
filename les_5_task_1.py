from collections import namedtuple
from statistics import mean

New_Company = namedtuple('New_Company', 'name profit avg')

lst = []
for i in range(int(input('Введите количество предприятий: '))):
    data = input('Введите название предприятия и прибыль по 4 кварталам:\n').split()
    lst.append(New_Company(data[0], data[1:], mean(map(int, data[1:3]))))

avg = mean([i.avg for i in lst])
print(f'Средняя прибыль всех предприятий: {avg}')

for i in lst:
    print(f'Предприятие: {i.name} \tСредняя прибыль за год: {i.avg}')

print(f'Предприятия с прибылью меньше средней: {[i.name for i in lst if i.avg < avg]}')

print(f'Предприятия с прибылью больше средней: {[i.name for i in lst if i.avg > avg]}')