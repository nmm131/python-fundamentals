def convert_dollars_to_dollars_and_cents(amount_in_dollars):
    dollars = int(amount_in_dollars // 1)
    quarters = int((amount_in_dollars - dollars) // 0.25)
    dimes = int((amount_in_dollars - dollars - quarters * 0.25) // 0.1)
    nickels = int((amount_in_dollars - dollars - quarters * 0.25 - dimes * 0.1) // 0.05)
    pennies = int(round((amount_in_dollars - dollars - quarters * 0.25 - dimes * 0.1 - nickels * 0.05) / 0.01))
    return dollars, quarters, dimes, nickels, pennies
