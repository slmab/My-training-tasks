# TODO здесь писать код

class Students:

    def __init__(self, student_name, group_number, student_grades):
        self.student_name = student_name.title()
        self.group_number = group_number
        self.student_grades = student_grades

    def average_rating(self):
        average_rating = sum(self.student_grades) / len(self.student_grades)
        return average_rating


def sort_key(some_tuple):
    return some_tuple[2]


students_average = []

for index in range(1, 11):
    name = input('Введите фамилию и имя студента: ')
    group = input('Введите группу студента: ')
    grades = input('Введите оценки студента через пробел: ').split()
    grades = [int(elem) for elem in grades]

    student = Students(name, group, grades)

    average_point = student.average_rating()
    students_average.append((student.student_name,
                             student.group_number, average_point))

print(sorted(students_average, key=sort_key))
