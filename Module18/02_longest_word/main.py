# TODO здесь писать код

text = input('Введите текст: ').split()
max_word = text[0]

for index in range(len(text)):
      if len(text[index]) > len(max_word):
            max_word = text[index]

print('Самое длинное слово в тексте:', max_word, end=', ')
print('его длина:', len(max_word), 'символов')

# TODO max() реализуем ручками =)
