shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

detail = input('Название детали: ').lower()
quantity = 0
cost = 0

for nested_list in shop:
        # TODO if detail in nested_list:
        if detail in nested_list:
                quantity += 1
                cost += nested_list[1]

print('Кол-во деталей:', quantity)
print('Общая стоимость:', cost)

# TODO здесь писать код
