# TODO здесь писать код

def print_num(number):
    if number == 0:
        return
    print_num(number - 1)
    print(number)


num = int(input('Введите максимальное число: '))

print_num(num)
