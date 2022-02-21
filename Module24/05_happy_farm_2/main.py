# TODO здесь писать код

class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print('Картошка {} сейчас {}'.format(
            self.index, Potato.states[self.state]
        ))


class PotatoGarden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка прорастает!')
        for i_potato in self.potatoes:
            i_potato.grow()

    def are_all_ripe(self):
        if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
            print('Картошка еще не созрела!\n')
        else:
            print('Вся картошка созрела, можно собирать!\n')


class Gardener:

    def __init__(self, name, bed):
        self.name = name
        self.bed = bed

    def take_care(self):
        self.bed.grow_all()

    def harvisting(self):
        self.bed.potatoes.clear()
        print('Картошка собрана\n')


my_garden = PotatoGarden(5)
garden = Gardener('Виктор', my_garden)
for _ in range(3):
    garden.take_care()
    my_garden.are_all_ripe()
garden.harvisting()
