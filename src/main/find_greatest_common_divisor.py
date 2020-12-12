def find_greatest_common_divisor(num_1, num_2):
    if num_1 < num_2:
        smallest_num = num_1
    else:
        smallest_num = num_2
    for common_divisor in range(1, smallest_num + 1):
        if num_1 % common_divisor == 0 and num_2 % common_divisor == 0:
            greatest_common_divisor = common_divisor
    return greatest_common_divisor
