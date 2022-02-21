# TODO здесь писать код

def sort_key(some_string):
    sort_string = some_string.split()
    return [int(sort_string[2])]


first_tour = open('first_tour.txt', 'r')
first_tour_list = []

for line in first_tour:
    first_tour_list.append(line.rstrip().split())

second_tour = []
for i_elem in first_tour_list[1:]:
    if int(i_elem[2]) > int(first_tour_list[0][0]):
        new_elem = '{0}. {1} {2}'.format(i_elem[1][0],
                                         i_elem[0], i_elem[2])
        second_tour.append(new_elem)

second_tour = sorted(second_tour, key=sort_key, reverse=True)
second_tour_file = open('second_tour.txt', 'w')
second_tour_file.write(str(len(second_tour)) + '\n')

for index, i_string in enumerate(second_tour, 1):
    i_string = '{0}) {1}\n'.format(index, i_string)
    second_tour[index - 1] = i_string
    second_tour_file.write(i_string)
