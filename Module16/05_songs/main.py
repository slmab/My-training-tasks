violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
# TODO здесь писать код

songs_quantity = int(input('Сколько песен выбрать? '))
total_duration = 0

for songs in range(songs_quantity):
    print('Название', songs + 1, 'песни:', end=' ')
    song_title = input()
    for song in violator_songs:
        # TODO if song_title in song:
        if song_title in song:
            total_duration += song[1]

print('Общее время звучания песен:', round(total_duration, 2), 'минут')

# Ok
