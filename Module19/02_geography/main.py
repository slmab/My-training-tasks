# TODO здесь писать код

quantity_countries = int(input('Кол-во стран: '))
country_dict = dict()

for country in range(quantity_countries):
    print(country + 1, 'страна:', end=' ')
    kit = input().split()
    for city in kit[1:]:
        country_dict[city] = kit[0]

for index in range(3):
    print(index + 1, 'город:', end=' ')
    town = input()
    country = country_dict.get(town, 0)
    if country == 0:
        print('По городу', town, 'данных нет')
    else:
        print('Город', town, 'расположен в стране', country)
