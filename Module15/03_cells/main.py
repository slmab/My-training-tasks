# TODO здесь писать код

cells_number = int(input('Кол-во клеток: '))
unsuitable_values = []

# на заметку: когда речь об индексе, используют аффикс/постфикс -- _idx
for cell_idx in range(cells_number):
    print('Эффективность', cell_idx + 1, 'клетки: ', end='')
    efficiency = int(input())
    if efficiency < (cell_idx + 1):
        unsuitable_values.append(efficiency)

print('Неподходящие значения: ', end='')
for value in unsuitable_values:
    print(value, end=' ')
