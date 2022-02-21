def digits_summa(number):
    summa = 0
    while number > 0:
        summa += number % 10
        number //= 10
    return summa

def digits_number(number):
    quantity = 0
    while number > 0:
        number //= 10
        quantity += 1
    return quantity

number = int(input('Введите число: '))

print('Сумма цифр:', digits_summa(abs(number)))
print('Кол-во цифр в числе:', digits_number(abs(number)))
print('Разность суммы и кол-ва цифр:', digits_summa(abs(number)) - digits_number(abs(number)))

# Ok
