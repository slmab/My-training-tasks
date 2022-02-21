# TODO здесь писать код

import random


class Home:
    people_food = 50
    money = 100
    cat_food = 30
    dirt = 0


class Cat:

    def __init__(self, name):
        self.name = name
        self.satiety = 30

    def eat(self):
        food_amount = random.randint(1, 10)
        Home.cat_food -= food_amount
        self.satiety += food_amount * 2

    def sleep(self):
        self.satiety -= 10

    def tear_wallpaper(self):
        Home.dirt += 5
        self.satiety -= 10

    def action(self):
        if self.satiety < 0:
            print('{} умер от голода.'.format(self.name))
            raise BaseException

        if self.satiety < 20:
            self.eat()
            print('Кот ест')
            return

        choice = random.randint(1, 2)
        if choice == 1:
            self.sleep()
            print('Кот спит')
        else:
            self.tear_wallpaper()
            print('Кот рвет обои')


class Person:

    def __init__(self, name):
        self.name = name
        self.satiety = 30
        self.happiness = 100

    def petting(self):
        self.happiness += 5
        self.satiety -= 10


class Husband(Person):

    def __init__(self, name):
        super().__init__(name)
        self.money_count = 0
        self.husband_food_count = 0

    def action(self):

        if self.satiety < 0:
            print('{} умер от голода.'.format(self.name))
            raise BaseException
        if self.happiness < 0:
            print('{} умер от депрессии'.format(self.name))
            raise BaseException
        if Home.dirt > 90:
            self.happiness -= 10

        choice = random.randint(1, 4)
        if self.satiety < 20:
            self.eat()
            print('Муж ест')
        elif Home.money < 50:
            self.work()
            print('Муж работает')
        elif self.happiness < 20:
            self.play()
            print('Муж играет')
        elif choice == 1:
            self.play()
            print('Муж играет')
        elif choice == 2:
            self.eat()
            print('Муж ест')
        elif choice == 3:
            self.work()
            print('Муж работает')
        else:
            self.petting()
            print('Муж гладит кота')

    def play(self):
        self.happiness += 20
        self.satiety -= 10

    def work(self):
        Home.money += 150
        self.satiety -= 10
        self.money_count += 150

    def eat(self):
        food_amount = random.randint(1, 30)
        Home.people_food -= food_amount
        self.satiety += food_amount
        self.husband_food_count += food_amount


class Wife(Person):

    def __init__(self, name):
        super().__init__(name)
        self.coat_count = 0
        self.wife_food_count = 0

    def action(self):

        if self.satiety < 0:
            print('{} умерла от голода.'.format(self.name))
            raise BaseException
        if self.happiness < 0:
            print('{} умерла от депрессии'.format(self.name))
            raise BaseException
        if Home.dirt > 90:
            self.happiness -= 10

        choice = random.randint(1, 5)
        if self.satiety < 20:
            self.eat()
            print('Жена ест')
        elif Home.people_food < 20 or Home.cat_food < 20:
            self.buy_products()
            print('Жена купила продукты')
        elif Home.dirt > 60:
            self.cleaning()
            print('Жена убирается')
        elif self.happiness < 20:
            self.buy_coat()
            print('Жена купила шубу')
        elif choice == 1:
            self.buy_coat()
            print('Жена купила шубу')
        elif choice == 2:
            self.petting()
            print('Жена гладит кота')
        elif choice == 3:
            self.buy_products()
            print('Жена купила продукты')
        elif choice == 4:
            self.eat()
            print('Жена ест')
        else:
            self.cleaning()
            print('Жена убирается')

    def buy_products(self):
        food = random.choice((10, 20, 30, 40, 50))
        Home.people_food += food
        Home.cat_food += food
        Home.money -= food * 2
        self.satiety -= 10

    def buy_coat(self):
        Home.money -= 350
        self.satiety -= 10
        self.happiness += 60
        self.coat_count += 1

    def cleaning(self):
        Home.dirt -= random.randint(1, 100)
        self.satiety -= 10

    def eat(self):
        food_amount = random.randint(1, 30)
        Home.people_food -= food_amount
        self.satiety += food_amount
        self.wife_food_count += food_amount


def life(family_list):
    for day in range(1, 366):
        print('День:', day)
        Home.dirt += 5
        for i_person in family_list:
            try:
                i_person.action()
            except:
                return False
    return True


home = Home()
husband = Husband('Иван')
wife = Wife('Ирина')
cat = Cat('Барсик')
family = [husband, wife, cat]

if life(family):
    print('Все выжили!')
    print(
        'Куплено шуб: {}. Еды съедено: {}. Денег заработано:'
        ' {}'.format(wife.coat_count,
                     wife.wife_food_count + husband.husband_food_count,
                     husband.money_count))
else:
    print('Упс')
