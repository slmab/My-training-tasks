# TODO здесь писать код

while True:
    username = input('Введите имя: ')
    print('Выберите действие:')
    print('Посмотреть текущий текст чата (введите 1) или Отправить сообщение (введите 2)', end=' ')
    answer = input()
    if answer == '1':
        try:
            with open('chat.txt', 'r', encoding='utf-8') as chat:
                for i_line in chat:
                    print(i_line.rstrip())
        except FileNotFoundError:
            print('Чат пуст!')
    elif answer == '2':
        message = input('Введите сообщение: ')
        with open('chat.txt', 'a', encoding='utf-8') as chat_write:
            chat_write.write('{}: {}\n'.format(username, message))
    else:
        print('Такой команды нет')
