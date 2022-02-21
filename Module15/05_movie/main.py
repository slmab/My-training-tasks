films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

numbers = int(input('Количество фильмов: '))
favorite_movies = []

for number in range(numbers):
    film = input('Введите название фильма: ')
    if film in films:
        favorite_movies.append(film)
    else:
        print('Ошибка')

print('Список любимых фильмов:', favorite_movies)

# TODO здесь писать код
# Ok
