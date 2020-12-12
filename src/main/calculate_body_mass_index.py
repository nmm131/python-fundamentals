def calculate_body_mass_index(weight):
    if weight < 18.5:
        return "Underweight"
    elif 18.5 <= weight < 25.0:
        return "Normal"
    elif 25.0 <= weight < 30.0:
        return "Overweight"
    else:
        return "Obese"
