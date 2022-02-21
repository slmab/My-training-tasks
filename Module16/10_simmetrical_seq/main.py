# TODO здесь писать код

numbers = int(input('Кол-во чисел: '))
numbers_list = []
reverse_numbers_list = []

for _ in range(numbers):
    number = int(input('Число: '))
    numbers_list.append(number)

print('Последовательность', numbers_list)

for number in range(len(numbers_list)- 1, -1, -1):
    reverse_numbers_list.append(numbers_list[number])

while True:
    if numbers_list == reverse_numbers_list:
        print('Последовательность симметричная')
        break
    elif numbers_list[len(numbers_list) - 1] == reverse_numbers_list[0]:
        reverse_numbers_list.remove(reverse_numbers_list[0])
    else:
        print('Нужно приписать чисел:', len(reverse_numbers_list))
        print('Сами числа:', end=' ')
        for number in range(len(reverse_numbers_list)):
            print(reverse_numbers_list[number], end=' ')
        break
