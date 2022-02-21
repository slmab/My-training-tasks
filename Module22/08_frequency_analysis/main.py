# TODO здесь писать код

def sort_key(some_string):
    sort_string = some_string.split()
    return [float(sort_string[1])]


file = open('text.txt', 'r')
new_line = ''

for line in file:
    for sym in line:
        if sym.isalpha():
            new_line += sym.lower()

new_line_set = set(new_line)
new_file = []

for i_sym in new_line_set:
    count_sym = new_line.count(i_sym)
    fraction = count_sym / len(new_line)
    new_file_str = '{} {}\n'.format(i_sym, round(fraction, 3))
    new_file.append(new_file_str)

sorted_new_file = sorted(new_file, key=sort_key, reverse=True)
analysis = open('analysis.txt', 'w')

for symbol in sorted_new_file:
    analysis.write(symbol)
