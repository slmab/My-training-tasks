guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

print('Сейчас на вечеринке', len(guests), 'человек:', guests)

request = input('Гость пришел или ушел? ')

while request.lower() != 'пора спать':
    if len(guests) <= 5:
        if request.lower() == 'пришел':
            name = input('Имя гостя: ')
            print('Привет,', name)
            guests.append(name)
        if request.lower() == 'ушел':
            name = input('Имя гостя: ')
            print('Пока,', name)
            guests.remove(name)
    else:
        if request.lower() == 'пришел':
            name = input('Имя гостя: ')
            print('Прости,', name, 'но мест нет')
        if request.lower() == 'ушел':
            name = input('Имя гостя: ')
            print('Пока,', name)
            guests.remove(name)
    request = input('Гость пришел или ушел? ')

print('Вечеринка закончилась, все легли спать')

# TODO здесь писать код
