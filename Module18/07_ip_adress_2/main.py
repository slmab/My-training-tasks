# TODO здесь писать код

while True:
    ip_address = input('Введите IP: ').split('.')
    if len(ip_address) != 4:
        print('Адресс - это четыре числа, разделенные точкой')
    else:
        for digit in ip_address:
            if not digit.isdecimal():
                print(digit, '- не целое число')
                break
            elif int(digit) < 0 or int(digit) > 255:
                print('Число', digit, 'выходит за рамки допустимого '
                                      'диапазона')
                break
        else:
            print('IP-адресс корректен')
            break
