violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

# TODO здесь писать код

songs_quantity = int(input('Сколько песен выбрать? '))
total_duration = 0

for number in range(songs_quantity):
    print('Введите название', number + 1, 'песни:', end=' ')
    song = input()
    duration = violator_songs.get(song, 0)
    if duration != 0:
        total_duration += duration
    else:
        print('Ошибка, такой песни нет в списке')

print('Общее время звучания песен:', round(total_duration, 2))

# TODO
# Сколько песен выбрать? 
# 1
# Введите название 1 песни: 
# Мурка
# Traceback (most recent call last):
#   File "main.py", line 21, in <module>
#     duration += violator_songs[song]
# KeyError: 'Мурка'

# dict.get(key, default)
