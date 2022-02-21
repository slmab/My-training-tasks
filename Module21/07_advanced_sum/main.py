# TODO здесь писать код

def elements_sum(*args):
    return sum(my_summ(args))


def my_summ(list_elements):
    result = []
    for elem in list_elements:
        if isinstance(elem, int):
            result.append(elem)
        else:
            result.extend(my_summ(elem))
    return result


print(elements_sum([[1, 2, [3]], [1], 3]))
print(elements_sum(1, 2, 3, 4, 5))
