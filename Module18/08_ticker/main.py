# TODO здесь писать код

string_first = input('Первая строка: ')
string_second = input('Вторая строка: ')
count = 0

for index in range(len(string_first)):
    if (string_first[index:] + string_first[:index]) == string_second:
        print('Вторая строка получается из первой со сдвигом', count)
        break
    count += 1
else:
    print('Вторую строку нельзя получить из первой с помощью циклического сдвига')
