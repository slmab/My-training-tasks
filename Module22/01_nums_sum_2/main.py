# TODO здесь писать код

with open('numbers.txt', 'r', encoding='utf-8') as task:
    summ = 0
    for line in task:
        if line.strip():
            summ += int(line)

with open('answer.txt', 'w', encoding='utf-8') as answer:
    answer.write(str(summ))
