# TODO здесь писать код

text = input('Введите строку: ')
count = 1
index = 0
compressed_string = ''

while index + 1 < len(text):
    if text[index] == text[index + 1]:
        count += 1
    else:
        compressed_string += text[index] + str(count)
        count = 1
    index += 1

print('Закодированная строка:', compressed_string + text[index] + str(count))
