# TODO здесь писать код

def checking_index(checking_text):
    return [i_index for i_index, sym in enumerate(checking_text) if is_prime(i_index) and i_index != 0]


def is_prime(number):
    for num in range(2, (number // 2) + 1):
        if number % num == 0:
            return False
    return True


text = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5}
# TODO читаем доку по isinstance()
# Сергей, добрый день, честно сказать, я не понял что здесь надо
# Почитать, если isinstance возвращает True, то условие выполняется,
# Иначе нет)

# а в качестве второго аргумента мы можем передать несколько типов?

if isinstance(text, str):
    text = text.split(', ')
    index_list = checking_index(text)
    for i_index in index_list:
        print(text[i_index], end=' ')

elif isinstance(text, dict):
    index_list = checking_index(text)
    keys_list = list(text.keys())
    for index in index_list:
        print(keys_list[index], ':', text[keys_list[index]], end=' ')

elif isinstance(text, list):
    index_list = checking_index(text)
    for i_index in index_list:
        print(text[i_index], end=' ')

elif isinstance(text, tuple):
    index_list = checking_index(text)
    for i_index in index_list:
        print(text[i_index], end=' ')
