# TODO здесь писать код


def new_tup(start_tup, elem):
    if elem in start_tup:
        if start_tup.count(elem) > 1:
            first_index = start_tup.index(elem)
            second_index = start_tup.index(elem, first_index + 1)
            return start_tup[first_index:second_index + 1]
        else:
            return start_tup[start_tup.index(elem):]
    else:
        return ()


tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 11, 12, 13, 14, 1, 15)
element = int(input('Введите элемент: '))
answer = new_tup(tup, element)
print(answer)

# Сергей, здравствуйте, у меня здесь возник вопрос:
# Когда я ввожу элемент с клавиатуры, то я думал, что его правильно
# в формате строки, но тогда не работает счетчик, так как формат
# элементов не совпадает. Как это можно учесть в коде?

# tuple()
