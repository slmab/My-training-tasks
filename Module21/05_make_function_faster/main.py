def calculating_math_func(data, some_dict=dict()):
    if data in some_dict:
        return some_dict[data]
    else:
        result = 1
        for index in range(1, data + 1):
            result *= index
        result /= data ** 3
        result = result ** 10
        some_dict[data] = result
        return result


# TODO оптимизировать функцию

your_number = int(input('Введите число '
                        '(для выхода введите 0): '))

while your_number != 0:
    answer = calculating_math_func(your_number)

    print(answer)

    print('Введите число (для выхода введите 0): ')
    your_number = int(input())
