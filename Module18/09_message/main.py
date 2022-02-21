# TODO здесь писать код

text = input('Сообщение: ').split()
punctuation_marks = '.,;:?!-()\''
new_text = []

for word in text:
    new_word = []
    flag = 1
    for index in range(len(word)):
        if word[index] in punctuation_marks:
            flag = 0
            length = len(new_word) + 1
        if flag == 1:
            new_word.insert(0, word[index])
        if flag == 0:
            new_word.insert(length, word[index])
    new_word = ''.join(new_word)
    new_text.append(new_word)

print(' '.join(new_text))

# TODO не идет ответ с примером
# Сообщение: 
# Хотя ,. возм:ожно и нет.
# Новое сообщение: ятоХ ,. нжо:мзово и тен.
# Да, не заметил((
# Как оказалось, не все так просто))
