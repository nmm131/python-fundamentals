def determine_if_year_is_a_leap_year(year):
    if_year_is_divisible_by_4 = year % 4 == 0
    if_year_is_divisible_by_100 = year % 100 == 0
    if_year_is_divisible_by_400 = year % 400 == 0
    return (if_year_is_divisible_by_4 and not if_year_is_divisible_by_100) or if_year_is_divisible_by_400
