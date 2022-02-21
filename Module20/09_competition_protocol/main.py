# TODO здесь писать код

recordings = int(input('Сколько записей вносится в протокол? '))
recordings_list = list()
scores_list = list()
names_list = list()

for index in range(recordings):
    print(index + 1, 'запись:', end=' ')
    recording = input().split()
    recordings_list.append(recording)

for i_score in recordings_list:
    scores_list.append(int(i_score[0]))
    names_list.append(i_score[1])

winner = ''
count = 0

while count != 3:
    max_score_index = scores_list.index(max(scores_list))
    if names_list[max_score_index] != winner:
        win = scores_list.pop(max_score_index)
        max_people = names_list[max_score_index]
        winner = names_list.pop(max_score_index)
        count += 1
        print('{0} место. {1} ({2})'.format(count, winner, win))
    else:
        scores_list.pop(max_score_index)
        names_list.pop(max_score_index)

# Странное решение, но, вроде, работает)