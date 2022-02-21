# TODO здесь писать код

while True:
    text = input('Придумайте пароль: ')
    check_upper = [symbol for symbol in text if symbol.isupper()]
    check_digit = [symbol for symbol in text if symbol.isdigit()]
    if (len(check_upper)) >= 1 and (len(check_digit) >= 3)\
            and (len(text) >= 8):
        print('Это надежный пароль!')
        break
    else:
        print('Пароль ненадежный. Попробуйте еще раз.')
