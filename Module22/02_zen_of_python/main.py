# TODO здесь писать код

with open('zen.txt', 'r', encoding='utf-8') as python_zen:
    philosophy = []
    for line in python_zen:
        philosophy.append(line.rstrip())

for line in philosophy[::-1]:
    print(line)
