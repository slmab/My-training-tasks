# TODO здесь писать код

vowel_letters_dictionary = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']

text = input('Введите текст: ')
vowel_letters_text = []

for symbol in text:
    if symbol.lower() in vowel_letters_dictionary:
        vowel_letters_text.append(symbol.lower())

print('Список гласных букв:', vowel_letters_text)
print('Длина списка:', len(vowel_letters_text))
