# Хде? =)
# Видимо забыл закоммитить))

friends_quantity = int(input('Кол-во друзей: '))
debts_quantity = int(input('Долговых расписок: '))
debts = [0 for debt in range(friends_quantity)]

for debt in range(debts_quantity):
    print(debt + 1, 'расписка')
    borrower = int(input('Кому: '))
    debtor = int(input('От кого: '))
    loan = int(input('Сколько: '))
    debts[borrower - 1] += loan
    debts[debtor - 1] -= loan

print('Баланс друзей:')

for friend in range(len(debts)):
    print(friend + 1, debts[friend])

# Ok
