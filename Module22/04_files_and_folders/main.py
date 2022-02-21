# TODO здесь писать код

import os


def file_sizes(path):
    files_stat = [0, 0, 0]

    for i_elem in os.listdir(path):
        new_path = os.path.join(path, i_elem)
        if os.path.isfile(new_path):
            file_size = os.path.getsize(new_path)
            files_stat[0] += file_size
            files_stat[1] += 1
        if os.path.isdir(new_path):
            result = file_sizes(new_path)
            files_stat[0] += result[0]
            files_stat[1] += result[1]
            files_stat[2] += 1
    return files_stat


file_name = 'Module 22'
abs_path = os.path.abspath(os.path.join('..', '..', '..', file_name))

answer = file_sizes(abs_path)

print('Размер каталога (в Кб):', answer[0] / 1024)
print('Количество файлов:', answer[1])
print('Количество подкаталогов:', answer[2])
