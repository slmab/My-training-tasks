# TODO здесь писать код

start_tuple = 3, 5, 2, 6, 1, 7, 8, 4, 10, 9

if all(isinstance(elem, int) for elem in start_tuple):
    print(sorted(start_tuple))
else:
    print(start_tuple)

# TODO 
# isinstance() -- внимательно пересмотрите условие
# sorted()
# Да, разница между новым и старым кодом колоссальная)