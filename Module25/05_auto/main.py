# TODO здесь писать код

import math


class Car:

    def __init__(self, x_coordinate, y_coordinate, angle):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.angle = angle * math.pi / 180

    def move(self, distance):
        self.x_coordinate += distance * math.cos(self.angle)
        self.y_coordinate += distance * math.sin(self.angle)
        print('Сейчас автомобиль находится в точке {}, {}'.format(
            self.x_coordinate, self.y_coordinate))

    def turn(self, mov_angle):
        self.angle = mov_angle * math.pi / 180


class Bus(Car):

    def __init__(self, x_coordinate, y_coordinate, angle):
        super().__init__(x_coordinate, y_coordinate, angle)
        self.money = 0
        self.passengers = 0

    def get_on(self, amount):
        self.passengers += amount
        print('Сейчас в автобусе {} пассажиров'.format(self.passengers))

    def get_out(self, amount):
        self.passengers -= amount
        print('Сейчас в автобусе {} пассажиров'.format(self.passengers))

    def move(self, distance):
        self.x_coordinate += distance * math.cos(self.angle)
        self.y_coordinate += distance * math.sin(self.angle)
        self.money += self.passengers * distance
        print('Сейчас автобус находится в точке {}, {}.'
              '\nЗаработано денег - {}'.format(
                self.x_coordinate, self.y_coordinate, self.money))


car = Car(0, 0, 0)
car.turn(45)
car.move(10)

bus = Bus(0, 0, 0)
bus.get_on(10)
bus.turn(45)
bus.move(10)
