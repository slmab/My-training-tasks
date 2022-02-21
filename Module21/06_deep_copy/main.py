import copy


def new_site(struct, names):
    for key in struct:
        if 'телефон' in struct[key]:
            struct[key] = struct[key].replace('телефон', names)

    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            new_site(sub_struct, names)
        else:
            return

    return struct


site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на телефон',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}

# TODO здесь писать код

site_quantity = int(input('Сколько сайтов? '))
site_list = []

while site_quantity != 0:
    site_quantity -= 1
    product = input('Введите название продукта для нового сайта: ')
    result = new_site(copy.deepcopy(site), product)
    site_list.append(result)
    for your_site in site_list:
        print(your_site)
