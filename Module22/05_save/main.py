# TODO здесь писать код

import os


def way_gen(some_way):
    return os.path.sep.join(some_way)


def work_with_file(path):
    if os.path.exists(path):
        choice = input('Вы действительно хотите перезаписать файл? ')
        if choice.lower() == 'да':
            answer_file = open(abs_way, 'w')
            answer_file.write(your_string)
            print('Файл успешно перезаписан!')
            answer_file.close()
    else:
        answer_file = open(abs_way, 'w')
        answer_file.write(your_string)
        print('Файл успешно сохранен!')
        answer_file.close()


your_string = input('Введите строку: ')
way = input('Куда хотите сохранить документ? Введите '
            'последовательность папок (через пробел): ').split()
file_name = input('Введите имя файла: ') + '.txt'

abs_way = os.path.abspath(os.path.join(os.path.sep, way_gen(way), file_name))

work_with_file(abs_way)
print('Содержимое файла')
print(open(abs_way, 'r').read())
