# TODO здесь писать код

word = input('Введите слово: ')

word = list(word)
length = len(word)
check = int(length / 2)
count = 0

for symbol in range(1, check + 1):
    if word[symbol - 1] == word[-symbol]:
        count += 1

if count == check:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')

# Ok
