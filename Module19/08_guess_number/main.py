# TODO здесь писать код

max_number = int(input('Введите максимальное число: '))
right_set = set()
wrong_set = set()

while True:
    print('Нужное число есть среди вот этих чисел:', end=' ')
    numbers_set = input().split()
    if numbers_set[0].lower() == 'помогите':
        print('Артем мог загадать следующие числа:', end=' ')
        for num in right_set:
            print(num, end=' ')
        break
    answer = input('Ответ Артема: ').lower()
    if answer == 'да':
        right_set.clear()
        for sym in numbers_set:
            right_set.add(sym)
    elif answer == 'нет':
        for sym in numbers_set:
            if sym in right_set:
                right_set.remove(sym)
    if len(right_set) == 1:
        print('Артем загадал число:', right_set.pop())
        break
