# TODO здесь писать код

quantity_video_card = int(input('Кол-во видео карт: '))
old_list = []
new_list = []

for number in range(quantity_video_card):
    print(number + 1, 'Видеокарта:', end=' ')
    title_video_card = int(input())
    old_list.append(title_video_card)

maximum = old_list[0]
for name in old_list:
    if name > maximum:
        maximum = name

for title in old_list:
    if title != maximum:
        new_list.append(title)

print('Старый список видеокарт:', old_list)
print('Новый список видеокарт:', new_list)

# Ok
