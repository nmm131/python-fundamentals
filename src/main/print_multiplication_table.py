def print_multiplication_table():
    for multiplier_1 in range (1, 10):
        for multiplier_2 in range (1, 10):
            product = multiplier_1 * multiplier_2
            print("{} x {} = {}".format(multiplier_1, multiplier_2, product))
    return
