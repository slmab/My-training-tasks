# TODO здесь писать код


def addendum():
    name = input('Введите имя: ').title()
    surname = input('Введите фамилию: ').title()
    phone_number = input('Введите номер телефона: ')
    if (name, surname) in phonebook_dict:
        print('Такой человек уже есть в списке контактов.')
    else:
        phonebook_dict[(name, surname)] = phone_number

    print('Текущий список контактов:', phonebook_dict)


def search():
    surname = input('Введите фамилию: ').title()
    for i_person in phonebook_dict:
        if surname in i_person:
            print(i_person[0], i_person[1], phonebook_dict[i_person])


phonebook_dict = dict()

while True:
    action = input('Выберите действие: Добавить контакт или '
                   'поиск по фамилии: ').lower()
    if action == 'добавить контакт':
        addendum()
    elif action == 'поиск':
        search()
    else:
        print('Нет такой команды.')
