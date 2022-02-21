# TODO здесь писать код

orders_number = int(input('Введите кол-во заказов: '))
orders_dict = dict()

for index in range(orders_number):
    print('{} заказ:'.format(index + 1), end=' ')
    order = input().split()
    if order[0] in orders_dict.keys():
        if order[1] in orders_dict[order[0]].keys():
            orders_dict[order[0]][order[1]] += int(order[2])
        else:
            orders_dict[order[0]][order[1]] = int(order[2])
    else:
        orders_dict[order[0]] = {order[1]: int(order[2])}

for key in sorted(orders_dict.keys()):
    print(key, end=':\n')
    for pizza in sorted(orders_dict[key].keys()):
        print('\t', pizza, ':', orders_dict[key][pizza])
