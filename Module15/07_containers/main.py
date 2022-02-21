# TODO здесь писать код

number_containers = int(input('Кол-во контейнеров: '))
containers_list = []

for container in range(number_containers):
    container_weight = int(input('Введите вес контейнера: '))
    if container_weight > 200:
        print('Вес контейнера превышает норму')
        container_weight = int(input('Введите вес контейнера: '))
        containers_list.append(container_weight)
    else:
        containers_list.append(container_weight)

containers_list.sort(reverse=True)
new_container = int(input('Введите вес нового контейнера: '))
count = 0

if new_container > 200:
    print('Вес контейнера превышает норму')
else:
    for number in containers_list:
        if number >= new_container:
            count += 1

print('Номер, куда встанет новый контейнер:', count + 1)

# Ok
