number = int(input('Введите число: '))

for divider in range(2, number + 1):
    if number % divider == 0:
        print('Наименьший делитель, отличный от единицы:', divider)
        break
#while True:
  #  if number % 2 == 0:
    #    print('Наименьший делитель, отличный от единицы: 2')
      #  break
    #else:
      #  divider = 1
       # while divider <= number:
         #   divider += 2
           # if number % divider == 0:
             #   print('Наименьший делитель, отличный от единицы:', divider)
               # break
       # break

# TODO не очень понимаю профит от этого алгоса,
# в принципе, достаточно функции с одним циклом
#Если сначала проверить 2, то потом можно исключить четные числа из проверки,
# Так быстрее выполняется код
# Тогда уж for

# Ok
