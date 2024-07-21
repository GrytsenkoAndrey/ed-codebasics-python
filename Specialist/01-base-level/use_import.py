import random

n1 = random.randint(1, 100)
n2 = random.randint(1, 100)
result = input(f'Сколько будет {n1} + {n2}? ')
test = result.replace('.', '', 1)

if not test.isdigit():
    print('Введите число!')
else:
    if result == test:
        result = int(result)
    else:
        result = float(result)

    if result == n1 + n2:
        print('Верно!')
    else:
        print('Неверно!')