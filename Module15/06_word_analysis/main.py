# TODO здесь писать код

word = input('Введите слово: ')
length = len(word)
count = 0

for i in range(length):
    if word.count(word[i]) == 1:
        count += 1

print('Количество уникальных букв:', count)

# TODO попробуйте str.count()
# Да, так код стал короче)
