# TODO здесь писать код
import random


class KillError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GlyuttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class Buddhist:
    __karma = 500

    def get_karma(self):
        return self.__karma

    def one_day(self):
        if random.choices((False, True), (5/10, 5/10))[0]:
            raise random.choice((KillError, DrunkError, CarCrashError,
                                 GlyuttonyError, DepressionError))
        else:
            return random.randint(1, 7)


buddhist = Buddhist()
bud_karma = 0
ideal = buddhist.get_karma()
day = 0
with open('karma.log', 'w', encoding='utf-8') as errors:
    while True:
        day += 1
        try:
            if bud_karma < ideal:
                bud_karma += buddhist.one_day()
            else:
                print('Просветление')
                break
        except KillError:
            errors.write('День {}. Ошибка KillError\n'.format(day))
        except DrunkError:
            errors.write('День {}. Ошибка DrunkError\n'.format(day))
        except CarCrashError:
            errors.write('День {}. Ошибка CarCrashError\n'.format(day))
        except GlyuttonyError:
            errors.write('День {}. Ошибка GlyutonnyError\n'.format(day))
        except DepressionError:
            errors.write('День {}. Ошибка DepressionError\n'.format(day))
