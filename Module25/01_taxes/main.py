# TODO здесь писать код

class Property:
    def __init__(self, worth):
        self.worth = worth

    def tax_calculation(self):
        return self.worth / 100


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        return self.worth / 1000


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        return self.worth / 200


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        return self.worth / 500


money = int(input('Сколько у вас денег? '))

apartment_price = int(input('Сколько стоит квартира? '))
apartment = Apartment(apartment_price)
apartment_tax = apartment.tax_calculation()

car_price = int(input('Сколько стоит машина? '))
car = Car(car_price)
car_tax = car.tax_calculation()

countryhouse_price = int(input('Сколько стоит загородный дом? '))
countryhouse = CountryHouse(countryhouse_price)
countryhouse_tax = countryhouse.tax_calculation()

print('Налог на квартиру: {}\nНалог на машину {}\nНалог на '
      'загородный дом {}'.format(apartment_tax, car_tax,
                                 countryhouse_tax))

if (apartment_tax + car_tax + countryhouse_tax) < money:
    print('Вам хватает денег, чтобы заплатить все налоги!')
else:
    print('Вам не хватает:', apartment_tax + car_tax + countryhouse_tax
          - money)
