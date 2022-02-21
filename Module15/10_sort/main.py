# TODO здесь писать код

numbers = int(input('Кол-во элементов списка: '))
numbers_list = []

for _ in range(numbers):
    number = int(input('Введите число: '))
    numbers_list.append(number)

print('Изначальный список:', numbers_list)
length = len(numbers_list)

for i in range(length):
    minimum = numbers_list[i]
    for j in range(i + 1, length):
        if numbers_list[j] < minimum:
            minimum = numbers_list[j]
            numbers_list[i], numbers_list[j] = numbers_list[j], numbers_list[i]

print('Отсортированный список:', numbers_list)

# Ok
