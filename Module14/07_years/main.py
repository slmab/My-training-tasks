start_year = int(input('Введите первый год: '))
stop_year = int(input('Введите второй год: '))

print('Года от', start_year, 'до', stop_year, 'с тремя одинаковыми цифрами:')

for year in range(start_year, stop_year + 1):
    calculation_year = year
    units = calculation_year % 10
    calculation_year //= 10
    tens = calculation_year % 10
    calculation_year //= 10
    hundreds = calculation_year % 10
    calculation_year //= 10
    thousands = calculation_year
    if (units == tens == hundreds == thousands):
        year = 0
    elif ((units == tens) and (units == hundreds or units == thousands))\
    or ((units == hundreds) and (units == thousands)) \
    or ((tens == hundreds) and (tens == thousands)):
        print(year)

# TODO а решите просто "в лоб" - статика очень эффективна здесь
# Честно сказать, ничего другого не приходит в голову, как это - "в лоб"?

# а это нарезать заведомо четырехзначное число с помощью арифметики без циклов

# Ok
