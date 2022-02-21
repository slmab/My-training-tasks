# TODO здесь писать код

import random


errors = [StopIteration, ArithmeticError, AssertionError,
          AttributeError, BufferError, EOFError, ImportError,
          LookupError, MemoryError, NameError, OSError]
numbers_summ = 0

with open('numbers.txt', 'w') as file:
    while numbers_summ <= 777:
        try:
            number = int(input('Введите число: '))
            numbers_summ += number
            choice = [False, True]
            choice_weight = [12, 1]
            if random.choices(choice, weights=choice_weight)[0]:
                raise random.choice(errors)
            file.write(str(number) + '\n')
        except:
            break
