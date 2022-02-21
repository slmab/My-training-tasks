# TODO здесь писать код

def move(numbers, start, end):
    if numbers == 1:
        print('Переложить диск 1 со стержня номер {0} на стержень номер {1}'.format(start, end))
        return
    move(numbers - 1, start, (6 - start - end))
    print('Переложить диск {0} со стержня номер {1} на стержень номер {2}'.format(numbers, start, end))
    move(numbers - 1, (6 - start - end), end)


disks_number = int(input('Введите кол-во дисков: '))
move(disks_number, 1, 3)
