# TODO здесь писать код

word = input('Введите строку: ').lower()
word = list(word)

first_h = word.index('h')
word.reverse()
last_h = word.index('h')

print(word[last_h + 1:len(word) - first_h - 1])
