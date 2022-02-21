students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def interest(students_dict):
    students_hobby = list()
    surnames_length = 0
    for hobby in students_dict.items():
        students_hobby.extend(hobby[1]['interests'])
        surnames_length += len(hobby[1]['surname'])
    return students_hobby, surnames_length


for index in students.items():
    print('ID студента: {0}; Возраст студента: {1}'.format(index[0],
                                                           index[1]['age']))

student_interests, surname_length = interest(students)
print('Интересы студентов:', student_interests,
      '\nОбщая длина всех фамилий студентов:', surname_length)

# TODO исправить код
