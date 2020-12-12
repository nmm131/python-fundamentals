from src.main.compute_the_area_of_a_circle import computing_the_area_of_a_circle
from src.main.time_in_seconds_to_time_in_minutes_and_seconds import time_in_seconds_to_time_in_minutes_and_seconds
from src.main.convert_fahrenheit_to_celsius import convert_fahrenheit_to_celsius
from src.main.get_current_time import get_current_time
from src.main.calculate_sales_tax_to_two_decimals import calculate_sales_tax_to_two_decimals
from src.main.compute_loan_payment import compute_loan_payment
from src.main.convert_dollars_to_dollars_and_cents import convert_dollars_to_dollars_and_cents
from src.main.convert_hexadecimal_to_decimal import convert_hexadecimal_to_decimal
from src.main.generate_a_random_character import generate_a_random_character
from src.main.addition_quiz import addition_quiz
from src.main.calculate_body_mass_index import calculate_body_mass_index
from src.main.compute_taxes import compute_taxes
from src.main.determine_divisibility_of_number_by_2_and_3 import determine_divisibility_of_number_by_2_and_3
from src.main.determine_if_year_is_a_leap_year import determine_if_year_is_a_leap_year
from src.main.play_the_number_lottery import play_the_number_lottery
from src.main.compute_chinese_zodiac import compute_chinese_zodiac
from src.main.addition_quiz_until_correct import addition_quiz_until_correct
from src.main.too_high_or_too_low_number_guessing_game import too_high_or_too_low_number_guessing_game


# Compute the area of a circle
radius = eval(input("Type a radius: "))
area = computing_the_area_of_a_circle(radius)
print("The area for the circle of radius {} is {}".format(radius, area))
print("\n")

# Convert time in seconds to time in minutes and seconds
seconds = eval(input("Type time in seconds: "))
minutes_and_seconds = time_in_seconds_to_time_in_minutes_and_seconds(seconds)
minutes = minutes_and_seconds[0]
seconds = minutes_and_seconds[1]
print("Time in minutes and seconds: {} min and {} sec".format(minutes, seconds))
print("\n")

# Convert fahrenheit to celsius
fahrenheit = eval(input("Type a fahrenheit: "))
celsius = convert_fahrenheit_to_celsius(fahrenheit)
print("Fahrenheit to Celsius: {:.2f}".format(celsius))
print("\n")

# Get current time
hours_and_minutes_and_seconds = get_current_time()
hours = hours_and_minutes_and_seconds[0]
minutes = hours_and_minutes_and_seconds[1]
seconds = hours_and_minutes_and_seconds[2]
print("{}:{}:{}".format(hours, minutes, seconds))
print("\n")

# Calculate sales tax to two decimals
price = eval(input("Type price in dollars: "))
sales_tax = calculate_sales_tax_to_two_decimals(price)
print("Sales Tax: ${:.2f}".format(sales_tax))
print("\n")

# Compute loan payments
interest_rate = eval(input("Type interest rate: "))
num_years = eval(input("Type number of years: "))
loan_amount = eval(input("Type loan amount: "))
monthly_loan_payment = compute_loan_payment(interest_rate, num_years, loan_amount)
yearly_loan_payment = monthly_loan_payment * 12
print("Monthly Payment: {:.2f}"
      "\nTotal Payment: {:.2f}".format(monthly_loan_payment, yearly_loan_payment))
print("\n")

# Convert dollars to dollars and cents
amount_in_dollars = eval(input("Enter an amount in dollars: "))
amount_in_dollars_and_cents = convert_dollars_to_dollars_and_cents(amount_in_dollars)
dollars = amount_in_dollars_and_cents[0]
quarters = amount_in_dollars_and_cents[1]
dimes = amount_in_dollars_and_cents[2]
nickels = amount_in_dollars_and_cents[3]
pennies = amount_in_dollars_and_cents[4]
print("{} dollar(s), {} quarter(s), {} dime(s), {} nickel(s) and {} penny[ies]"
      .format(dollars, quarters, dimes, nickels, pennies))
print("\n")

# Convert hexadecimal to decimal
hexadecimal = input("Type a hexadecimal digit (e.g. 00 or FF): ")
decimal = convert_hexadecimal_to_decimal(hexadecimal)
print("\n")

# Generate a random character
random_char = generate_a_random_character()
print("Random character: {}".format(random_char))
print("\n")

# Quiz the user on addition
is_answer_correct = addition_quiz()
print(is_answer_correct)
print("\n")

# Calculate body mass index
weight = eval(input("Type your weight in lbs: "))
bmi = calculate_body_mass_index(weight)
print(bmi)
print("\n")

# Compute taxes
taxes = compute_taxes()
print("Tax: ${}".format(taxes))
print("\n")

# Determine divisibility of number by 2 and 3
number = eval(input("Type a number: "))
divisibility_by_2_and_3 = determine_divisibility_of_number_by_2_and_3(number)
print(divisibility_by_2_and_3)
print("\n")

# Determine if year is a leap year
year = eval(input("Type a year: "))
is_leap_year = determine_if_year_is_a_leap_year(year)
print(is_leap_year)
print("\n")

# Play the number lottery
two_digit_number = eval(input("Type a two-digit number: "))
lottery_winnings = play_the_number_lottery(two_digit_number)
print("You won: ${}".format(lottery_winnings))
print("\n")

# Compute chinese zodiac
year = eval(input("Type a year: "))
chinese_zodiac = compute_chinese_zodiac(year)
print("Your animal is: {}".format(chinese_zodiac))
print("\n")

# Quiz the user on addition until correct
is_answer_correct = addition_quiz_until_correct()
print(is_answer_correct)
print("\n")

# Ask the user to guess a random number between 0 and 100
too_high_or_too_low_number_guessing_game()
