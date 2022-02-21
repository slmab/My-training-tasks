# TODO здесь писать код

list_length = int(input('Введите длину списка: '))

numbers_list = [1 if index % 2 == 0 else index % 5 for index in range(list_length)]

print('Результат:', numbers_list)
