import random


def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x


try:
    with open('coordinates.txt', 'r') as file:
        with open('result.txt', 'w') as file_2:
            for index, line in enumerate(file, 1):
                try:
                    nums_list = line.split()
                    res1 = round(f(int(nums_list[0]), int(nums_list[1])), 5)
                    res2 = round(f2(int(nums_list[0]), int(nums_list[1])), 5)
                    number = random.randint(0, 100)
                    my_list = sorted([res1, res2, number])
                    file_2.write(' '.join(str(my_list)) + '\n')
                except ZeroDivisionError:
                    file_2.write('\n')
                    print('В строке {} возникло деление на ноль'.format(index))
except FileNotFoundError:
    print('Не найден файл с координатами.')

# TODO отредактировать и исправить программу
