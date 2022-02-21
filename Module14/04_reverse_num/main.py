def rev_num(number):
    part_integer = int(number)
    part_float = number - part_integer
    integer_reversed = 0
    float_reversed = 0
    while part_integer > 0:
        integer_reversed = integer_reversed * 10 + part_integer % 10
        part_integer //= 10
    while part_float > 1e-8:
        float_reversed = float_reversed / 10 + int(part_float * 10) / 10
        part_float = (part_float * 10) % 1
    reversed_number = integer_reversed + float_reversed
    return reversed_number


first_number = float(input('Введите первое число: '))
second_number = float(input('Введите второе число: '))

first_number_reversed = rev_num(first_number)
second_number_reversed = rev_num(second_number)
print('Первое число наоборот:', first_number_reversed)
print('Второе число наоборот:', second_number_reversed)
print('Сумма:', first_number_reversed + second_number_reversed)

# Ok как относитесь к str.replace() -- ак это относилось к предыдущей версии
# Метод интересный, не слышал про такой, но как его использовать не придумал((
# Зато придумал как сократить код задачи в 2 раза)

# TODO
# а он точно теперь рабочий?
# кстати, срезы мы не проходили =)
# решите задание пройденными средствами

# Я не нашел где старое решение не работает, у меня все ок, вроде) -- не передергивайте; решаем пройденными средствами =))
# Но новое решение вот)

# Ok
