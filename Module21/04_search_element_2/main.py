# TODO здесь писать код

def find_key(struct, key, max_depth=1e9):
    if max_depth == 0:
        result = 'На заданной глубине такого ключа нет.'
        return result
    else:
        max_depth -= 1
        if key in struct:
            return struct[key]

        for sub_struct in struct.values():
            if isinstance(sub_struct, dict):
                result = find_key(sub_struct, key, max_depth)
                if result:
                    break
        else:
            result = None

        return result


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

user_key = input('Какой ключ ищем? ')
depth_answer = input('Вы хотите ввести максимальную глубину поиска? ')
if depth_answer.lower() == 'да':
    depth = int(input('Введите максимальную глубину поиска: '))
    value = find_key(site, user_key, depth)
else:
    value = find_key(site, user_key)

if value:
    print(value)
else:
    print('Такого ключа нет.')
