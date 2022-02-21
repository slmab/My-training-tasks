# TODO здесь писать код

def histogram(string):
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
    return sym_dict


def inverted_histogram(direct_dict):
    inverted_dict = dict()
    for key in (direct_dict.keys()):
        if direct_dict[key] in inverted_dict:
            inverted_dict[direct_dict[key]].append(key)
        else:
            inverted_dict[direct_dict[key]] = [key]
    return inverted_dict


text = input('Введите текст: ').lower()
first_dict = histogram(text)
inverted = inverted_histogram(first_dict)

for i_sym in sorted(first_dict.keys()):
    print(i_sym, ':', first_dict[i_sym])

for i_sym in sorted(inverted.keys()):
    print(i_sym, ':', inverted[i_sym])
