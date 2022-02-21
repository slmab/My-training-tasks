# TODO здесь писать код

import os


def find_zen(cur_path, file_name):
    for elem in os.listdir(cur_path):
        path = os.path.join(cur_path, elem)
        if file_name == elem:
            return path
        if os.path.isdir(path):
            print('Это директория')
            result = find_zen(path, file_name)
            if result:
                break
    else:
        result = None
    return result


def rarest_letter(some_list):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    min_let = 10000
    itself_letter = 'a'

    for letter in alphabet:
        letter_count = 0
        for string in some_list:
            letter_count += string.count(letter)
        if letter_count < min_let:
            min_let = letter_count
            itself_letter = letter

    return itself_letter


zen_path = find_zen(os.path.abspath(os.path.join('..', '02_zen_of_python')),
                    'zen.txt')

with open(zen_path, 'r', encoding='utf-8') as python_zen:
    philosophy = []
    for line_zen in python_zen:
        philosophy.append(line_zen.rstrip())

count_lines = len(philosophy)
print('Число строк:', count_lines)
count_letters = sum([1 for i in range(len(philosophy))
                     for let in philosophy[i] if let.isalpha()])
print('Число букв:', count_letters)
count_words = len([word for i in range(len(philosophy))
                   for word in philosophy[i].split()])
print('Число слов:', count_words)

rare_letter = rarest_letter(philosophy)

print('Самая редкая буква:', rare_letter)
