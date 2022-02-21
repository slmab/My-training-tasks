# TODO здесь писать код

people_quantity = int(input('Кол-во человек: '))
people_counter = int(input('Какое число в считалке? '))
print('Значит выбывает каждый', people_counter, 'человек')

people_list = [man for man in range(1, 6)]
working_list = people_list
count = 0

print('Текущий круг людей:', working_list)
print('Начало счета с номера 1')

while len(working_list) > 1:
    for symbol in range(len(working_list)):
        count += 1
        if count == people_counter:
            remove_element = working_list[symbol]
            print('Выбывает игрок под номером:', remove_element)
            index = working_list.index(remove_element)
            if index + 1 >= len(working_list):
                next_elem = working_list[0]
            else:
                next_elem = working_list[index + 1]
            working_list.remove(remove_element)
            if len(working_list) == 1:
                break
            count = 0
            print('\nТекущий круг людей:', working_list)
            print('Начало счета с номера', next_elem)

print('\nОстался человек под номером', working_list[0])
