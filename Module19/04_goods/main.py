goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# TODO здесь писать код

keys = goods.keys()

for number in keys:
    total_number = 0
    total_price = 0
    for index in range(len(store[goods[number]])):
        amount = store[goods[number]][index]['quantity']
        cost = store[goods[number]][index]['price'] * amount
        total_number += amount
        total_price += cost
    print('{0} - {1} шт, стоимость {2} руб'.format(number, total_number, total_price))
