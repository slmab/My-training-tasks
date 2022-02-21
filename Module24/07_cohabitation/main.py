# TODO здесь писать код
import random


class Human:

    def __init__(self, name, house):
        self.name = name
        self.house = house
        self.satiety = 50

    def eat(self):
        self.satiety += 5
        self.house.food -= 5
        print('{} поел. Сытость {},  еды в доме {}'.format(self.name,
                                                           self.satiety, Home.food))

    def work(self):
        self.satiety -= 5
        self.house.money += 5
        print('{} поработал. Сытость {}, денег в доме {}'.format(
            self.name, self.satiety, Home.money))

    def play(self):
        self.satiety -= 5
        print('{} поиграл. Сытость {}'.format(self.name, self.satiety))

    def purchases(self):
        self.house.food += 5
        self.house.money -= 5
        print('{} сходил за продуктами. Еды в доме {}, денег в доме '
              '{}'.format(self.name, Home.food, Home.money))


class Home:
    food = 50
    money = 0


def life(neighbors_list):
    for _ in range(365):
        for i_person in neighbors_list:
            if i_person.satiety <= 0:
                print('Человек умер.')
                return False
            choice = random.randint(1, 6)
            if i_person.satiety < 20:
                i_person.eat()
            elif Home.food < 10:
                i_person.purchases()
            elif Home.money < 50:
                i_person.work()
            elif choice == 1:
                i_person.work()
            elif choice == 2:
                i_person.eat()
            else:
                i_person.play()
    return True


home = Home
artem = Human('Артем', home)
neighbour = Human('Иван', home)
neighbors = [artem, neighbour]

if life(neighbors):
    print('Все выжили!')
else:
    print('Не стоит так жить, сосед умер')
