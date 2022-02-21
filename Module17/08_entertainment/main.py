# TODO здесь писать код

import random

sticks_number = int(input('Кол-во палок: '))
throws_number = int(input('Кол-во бросков: '))
sticks_list = ['|' for _ in range(sticks_number)]

for throw in range(throws_number):
    print('Бросок', throw + 1)
    left_stick = random.randint(0, sticks_number)
    right_stick = random.randint(left_stick, sticks_number)
    if left_stick == right_stick:
        sticks_list[left_stick:right_stick + 1] = '.'
    else:
        sticks_list[left_stick:right_stick] = '.' * (right_stick - left_stick)
    print('Сбиты палки с номера', left_stick + 1, 'по номер', right_stick)
    print(sticks_list)
