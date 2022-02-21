# TODO здесь писать код

first_list = []
second_list = []

for elem in range(3):
    digit = int(input('Введите число для первого списка: '))
    first_list.append(digit)

for elem in range(7):
    digit = int(input('Введите число для второго списка: '))
    second_list.append(digit)

first_list.extend(second_list)

for symbol in first_list:
    while first_list.count(symbol) != 1:
        first_list.remove(symbol)

print(first_list)
