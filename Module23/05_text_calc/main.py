# TODO здесь писать код

def operation(numbers_list):
    if numbers_list[1] == '+':
        return int(numbers_list[0]) + int(numbers_list[2])
    elif numbers_list[1] == '-':
        return int(numbers_list[0]) - int(numbers_list[2])
    elif numbers_list[1] == '*':
        return int(numbers_list[0]) * int(numbers_list[2])
    elif numbers_list[1] == '/':
        return int(numbers_list[0]) / int(numbers_list[2])
    elif numbers_list[1] == '//':
        return int(numbers_list[0]) // int(numbers_list[2])
    elif numbers_list[1] == '%':
        return int(numbers_list[0]) % int(numbers_list[2])
    else:
        raise SyntaxError


result = 0
with open('calc.txt', 'r', encoding='utf-8') as calculator:
    for i_line in calculator:
        try:
            i_line_list = i_line.split()
            if len(i_line_list) != 3:
                raise IndexError
            result += operation(i_line_list)
        except (IndexError, ValueError, SyntaxError, ZeroDivisionError):
            print('В строке', i_line.rstrip(), 'ошибка')
    print('Итоговая сумма =', result)
