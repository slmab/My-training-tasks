# TODO здесь писать код

base = {
    ('сидоров', 'никита'): 35,
    ('сидорова', 'алина'): 34,
    ('сидоров', 'павел'): 10,
    ('иванов', 'петр'): 28,
    ('иванова', 'светлана'): 25,
    ('петров', 'александр'): 21,
    ('смирнов', 'алексей'): 25,
    ('смирнова', 'татьяна'): 26,
    ('смирнова', 'ксения'): 22,
}

surname_input = input('Введите фамилию: ').lower()

for surname, name in base.keys():
    if (surname_input == surname)\
            or (surname_input + 'а' == surname)\
            or (surname_input.replace('ий', 'ая') == surname) \
            or (surname_input.replace('ая', 'ий') == surname) \
            or (surname_input[:len(surname_input) - 1] == surname):
        print(surname.title(), name.title(), base[(surname, name)])

# Здесь мне что-то никак не придумать, как вывести сообщение
# об ошибке, если ввести фамилию которой нет в словаре
