# TODO здесь писать код

class Parent:

    def __init__(self, name, age, children):
        self.name = name
        self.age = age
        self.children = children

    def print_info(self):
        print('Имя: {}\nВозраст: {}\nДети: {}'.format(
            self.name, self.age, [(kid.child_name, kid.child_age)
                                  for kid in self.children]))

    def calm(self):
        for kid in self.children:
            kid.state_calm = True

    def eat(self):
        for kid in self.children:
            kid.state_hungry = False


class Child:

    def __init__(self, name, age):
        self.child_name = name
        self.child_age = age
        self.state_calm = False
        self.state_hungry = True

    def print_information(self):
        print('Имя {}, Возраст {}, психологическое состояние {}, '
              'хочет ли есть {}'.format(self.child_name, self.child_age,
                                        self.state_calm, self.state_hungry))


parent_name = input('Введите имя родителя: ')
parent_age = int(input('Введите возраст родителя: '))
answer = input('У вас есть дети (если да, то сколько)? ').split()

if answer[0].lower() == 'нет':
    parent = Parent(parent_name, parent_age, [])

elif answer[0].lower() == 'да':
    children_list = []
    answer[1] = int(answer[1])
    for _ in range(answer[1]):
        kid_name = input('Введите имя ребенка:')
        kid_age = int(input('Введите возраст ребенка: '))
        if parent_age - kid_age < 16:
            print('Ошибка, слишком маленькая разница в возрасте.')
        else:
            child = Child(kid_name, kid_age)
            children_list.append(child)
    parent = Parent(parent_name, parent_age, children_list)

else:
    print('Ошибка ввода')

parent.print_info()

for kid in children_list:
    kid.print_information()

parent.calm()
parent.eat()

for kid in children_list:
    kid.print_information()
