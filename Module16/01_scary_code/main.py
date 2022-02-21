main_list = [1, 5, 3]
first_side_list = [1, 5, 1, 5]
second_side_list = [1, 3, 1, 5, 3, 3]

main_list.extend(first_side_list)

print('Кол-во цифр 5 при первом объединении:', main_list.count(5))

# TODO срочно читаем ман по list.remove()
# Это к тому что remove удаляет первый элемент и циклом for нельзя
# удалить два соседних элемента?
# for digit in main_list:
#     if digit == 5:
#         main_list.remove(digit)


# жестко вы с интерпретатором, так более гуманно: while 5 in main_list:
while main_list.count(5) != 0:
    main_list.remove(5)

main_list.extend(second_side_list)

print('Кол-во цифр 3 при первом объединении:', main_list.count(3))
print('Итоговый список:', main_list)

# TODO переписать программу
