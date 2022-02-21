# TODO здесь писать код

pair_quantity = int(input('Введите количество человек: '))
tree = dict()
check = dict()

for index in range(pair_quantity - 1):
    print('{} пара:'.format(index + 1), end=' ')
    pair = input().split()
    tree[pair[0]] = pair[1]
    check[pair[0]] = 0
    check[pair[1]] = 0

for index in tree.keys():
    relative = index
    while relative in tree:
        relative = tree[relative]
        check[index] += 1

for index in sorted(check):
    print(index, check[index])
