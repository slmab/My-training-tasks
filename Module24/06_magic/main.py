# TODO здесь писать код

class Water:

    def __str__(self):
        return 'Water'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Vapor()
        elif isinstance(other, Earth):
            return Dirt()
        else:
            return None


class Air:

    def __str__(self):
        return 'Air'

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        else:
            return None


class Fire:

    def __str__(self):
        return 'Fair'

    def __add__(self, other):
        if isinstance(other, Water):
            return Vapor()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Earth):
            return Lava()
        else:
            return None


class Earth:

    def __str__(self):
        return 'Earth'

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        else:
            return None


class Storm:

    def __str__(self):
        return 'Storm'


class Vapor:

    def __str__(self):
        return 'Vapor'


class Dirt:

    def __str__(self):
        return 'Dirt'


class Lightning:

    def __str__(self):
        return 'Lightning'


class Dust:

    def __str__(self):
        return 'Dust'

    def __add__(self, other):
        if isinstance(other, Lightning):
            return 'Fulgurite'
        if isinstance(other, Air):
            return 'Dust storm'


class Lava:

    def __str__(self):
        return 'Lava'


some_water = Water()
some_air = Air()
some_earth = Earth()
some_fire = Fire()

print(some_earth + some_air + some_air)
