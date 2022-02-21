# TODO здесь писать код

dictionary = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п',
              'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'щ', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

text = input('Введите текст: ')
new_text = ''

for symbol_idx in range(len(text)):
    if text[symbol_idx] in dictionary:
        index = dictionary.index(text[symbol_idx])
        if index <= 29:
            new_text += dictionary[index + 3]
        else:
            new_text += dictionary[index - 30]
    else:
        new_text += text[symbol_idx]

print(new_text)
