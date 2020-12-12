def compute_loan_payment(interest_rate, num_years, loan_amount):
    monthly_interest_rate = interest_rate / 100
    monthly_payment = (loan_amount * monthly_interest_rate) / \
                      (1 - (1 / ((1 + monthly_interest_rate)**(num_years * 12))))
    return monthly_payment
