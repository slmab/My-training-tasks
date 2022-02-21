# TODO здесь писать код

text = input('Введите строку: ')
check = []

for sym in text:
    if sym in check:
        check.remove(sym)
    else:
        check.append(sym)

if len(check) > 1:
    print('Нельзя сделать палиндром')
else:
    print('Можно сделать палиндром')
