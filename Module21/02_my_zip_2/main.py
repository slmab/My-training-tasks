# TODO здесь писать код

def shortest_seq_range(new_list):
    return min([len(elem) for elem in new_list])


def my_zip(*args):
    new_elem = [[i for i in elem] for elem in args]
    length = shortest_seq_range(new_elem)
    new_list = [tuple([new_elem[j_dx][i_dx] for j_dx in range(len(new_elem))]) for i_dx in range(length)]
    return new_list


some_list = [1, 2, 3, 4, 5]
some_dict = {1: 's', 2: 'q', 3: 4}
some_tuple = (1, 2, 3, 4, 5)

myzip = my_zip(some_list, some_tuple, some_dict)

print(myzip)
