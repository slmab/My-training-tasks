# TODO здесь писать код
import random


class Warriors:

    def __init__(self, name):
        self.name = name
        self.health_points = 100
        self.attack = 20

    # TODO самобичевание? =) self.attack
    def damage(self, target):
        target.health_points -= 20

    # TODO def is_alive():
    def is_alive(self):
        if self.health_points > 0:
            return True
        else:
            print('Юнит {} погиб'.format(self.name))
            return False


warrior_1 = Warriors('warrior_1')
warrior_2 = Warriors('warrior_2')

while True:
    warriors = (1, 2)
    choice = random.choice(warriors)
    if warrior_1.is_alive() and warrior_2.is_alive():
        if choice == 1:
            print('Аттакует первый юнит.')
            warrior_1.damage(warrior_2)
            print('У второго юнита осталось {} единиц здоровья'.format(
            warrior_2.health_points))
        elif choice == 2:
            print('Аттакует второй юнит.')
            warrior_2.damage(warrior_1)
            print('У первого юнита осталось {} единиц здоровья'.format(
            warrior_1.health_points))
    else:
        break
