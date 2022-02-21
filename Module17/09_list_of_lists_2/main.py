nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

# TODO здесь писать код

new_nice_list = [nice_list[global_row][row][col] for global_row in range(2) for row in range(3)
                 for col in range(3)]

print('Ответ:', new_nice_list)
