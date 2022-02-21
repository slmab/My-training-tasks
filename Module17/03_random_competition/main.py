# TODO здесь писать код

import random

team_first = [round(random.uniform(5, 10), 2) for _ in range(10)]
team_second = [round(random.uniform(5, 10), 2) for _ in range(10)]
winners_list = [team_first[index] if team_first[index] > team_second[index]
                else team_second[index] for index in range(10)]

print('Первая команда:', team_first)
print('Вторая команда:', team_second)
print('Победители тура:', winners_list)
