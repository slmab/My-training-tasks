# TODO здесь писать код

first_class = [man for man in range(160, 177, 2)]
second_class = [man for man in range(162, 181, 3)]
first_class.extend(second_class)

for man_idx in range(len(first_class)):
    for woman_idx in range(man_idx + 1, len(first_class)):
        if first_class[woman_idx] < first_class[man_idx]:
            first_class[man_idx], first_class[woman_idx] = first_class[woman_idx], first_class[man_idx]

print('Итоговая шеренга:', first_class)
