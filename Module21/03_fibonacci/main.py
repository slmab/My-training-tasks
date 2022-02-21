# TODO здесь писать код

def fibonacci(position):
    new_list = [1, 1]
    while position - 2 != 0:
        position -= 1
        new_list.append(new_list[-1] + new_list[-2])
    return new_list


num_pos = int(input('Введите позицию числа в ряде Фибоначчи: '))
your_number = fibonacci(num_pos)[-1]

print(your_number)
