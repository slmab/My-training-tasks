# TODO здесь писать код

numbers = int(input('Кол-во чисел: '))
numbers_list = [int(input('Введите число: ')) for _ in range(numbers)]

while 0 in numbers_list:
    numbers_list.remove(0)

print(numbers_list)
