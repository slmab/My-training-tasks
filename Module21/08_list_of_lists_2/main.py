nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

# TODO здесь писать код
def simple_list(complex_list):
    result = []
    for elem in complex_list:
        if isinstance(elem, int):
            result.append(elem)
        else:
            result.extend(simple_list(elem))
    return result

new_list = simple_list(nice_list)

print(new_list)