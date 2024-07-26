r = input('Играем? Нажми N для выхода или (1, 2, 3) для выбора сложности ')

if r == 'N':
    print('Пока!')
else:
    print('Игра началась! ', end='')
    if int(r) == 1:
        print('Сложность 1')
    elif int(r) == 2:
        print('Сложность 2')
    elif int(r) == 3:
        print('Сложность 3')
    else:
        print('Неверный ввод')
