import random

n1 = random.randint(1, 100)
n2 = random.randint(1, 100)
result = input(f'Сколько будет {n1} + {n2}? ')
if int(result) == n1 + n2:
    print('Верно!')
else:
    print('Неверно!')