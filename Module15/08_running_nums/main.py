# TODO здесь писать код

numbers = int(input('Кол-во элементов списка: '))
shift = int(input('Сдвиг: '))
number_list = []

for number in range(numbers):
    elem = int(input('Введите число: '))
    number_list.append(elem)

print('Изначальный список:', number_list)

for _ in range(shift):
    number_list.insert(0, number_list.pop())

print('Сдвинутый список:', number_list)

# Ok
