def compute_taxes():
    filing_status = eval(input("What is your filing status (\n 0: single filers"
                               "\n 1: married filing jointly"
                               "\n 2: married filing separately"
                               "\n 3: head of household"
                               "): "))
    salary = eval(input("What is your salary: "))
    if filing_status == 0:
        if salary <= 8350:
            tax = 0.1
        elif 8351 <= salary <= 33950:
            tax = 0.15
        elif 33951 <= salary <= 82250:
            tax = 0.25
        elif 82251 <= salary <= 171550:
            tax = 0.28
        elif 171551 <= salary <= 372950:
            tax = 0.33
        else:
            tax = .35
    elif filing_status == 1:
        if salary <= 16700:
            tax = 0.1
        elif 16701 <= salary <= 67900:
            tax = 0.15
        elif 67901 <= salary <= 137050:
            tax = 0.25
        elif 137051 <= salary <= 208850:
            tax = 0.28
        elif 208851 <= salary <= 372950:
            tax = 0.33
        else:
            tax = .35
    elif filing_status == 2:
        if salary <= 8350:
            tax = 0.1
        elif 8351 <= salary <= 33950:
            tax = 0.15
        elif 33951 <= salary <= 68525:
            tax = 0.25
        elif 68526 <= salary <= 104425:
            tax = 0.28
        elif 104426 <= salary <= 186475:
            tax = 0.33
        else:
            tax = .35
    elif filing_status == 3:
        if salary <= 11950:
            tax = 0.1
        elif 11951 <= salary <= 45500:
            tax = 0.15
        elif 45501 <= salary <= 117450:
            tax = 0.25
        elif 117451 <= salary <= 190200:
            tax = 0.28
        elif 190201 <= salary <= 372950:
            tax = 0.33
        else:
            tax = .35
    else:
        return "Incorrect status!"
    taxes = salary * tax
    return taxes
