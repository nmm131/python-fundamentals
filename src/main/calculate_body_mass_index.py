def calculate_body_mass_index(weight_in_kilograms, height_in_meters):
    bmi = weight_in_kilograms / (height_in_meters * height_in_meters)
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25.0:
        return "Normal"
    elif 25.0 <= bmi < 30.0:
        return "Overweight"
    else:
        return "Obese"
