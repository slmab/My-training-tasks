# TODO здесь писать код

pair_quantity = int(input('Введите количество пар слов: '))
pair_dict = dict()

for index in range(pair_quantity):
    print('{} пара:'.format(index + 1), end=' ')
    pair = input().lower().split(' - ')
    pair_dict[pair[0]] = pair[1]

pair_inverted = {pair_dict[index]: index for index in pair_dict}

while True:
    word = input('Введите слово: ').lower()
    if word in pair_dict:
        print('Синоним:', pair_dict[word].title())
        break
    elif word in pair_inverted:
        print('Синоним:', pair_inverted[word].title())
        break
    else:
        print('Такого слова нет в словаре.')

# TODO не проще ли сразу synonym_1: synonym_2, synonym_2: synonym_1 ?
# if synonym in ...?
# может что-то недопонял))

# Зачем два словаря, если все прекрасно вмещается в один
