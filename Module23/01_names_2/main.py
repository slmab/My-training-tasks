# TODO здесь писать код
import logging


logging.basicConfig(filename='errors.log')
sym_sum = 0
try:
    with open('people.txt', 'r') as people_file:
        for index, i_line in enumerate(people_file, 1):
            try:
                length = len(i_line)
                if i_line.endswith('\n'):
                    length -= 1
                if length < 3:
                    raise BaseException
                sym_sum += length
            except BaseException:
                print(('Длина {} строки меньше 3 символов'.format(index)))
                logging.exception('BaseException')

except FileNotFoundError:
    print('Файл не найден.')
    logging.exception('FileNotFound')
finally:
    print('Найденная сумма символов:', sym_sum)
