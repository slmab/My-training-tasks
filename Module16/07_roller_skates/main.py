# TODO здесь писать код

skates_number = int(input('Кол-во коньков: '))
skate_list = []

for skate in range(skates_number):
    print('Размер', skate + 1, 'пары:', end=' ')
    skate_size = int(input())
    skate_list.append(skate_size)

people_number = int(input('Кол-во людей: '))
people_list = []
people_count = 0

for people in range(people_number):
    print('Размер ноги', people + 1, 'человека:', end=' ')
    foot_size = int(input())
    people_list.append(foot_size)

for skate in skate_list:
    for foot in people_list:
        if skate >= foot:
            people_count += 1
            break

print('Наибольшее кол-во людей, которые могут взять ролики:', people_count)
