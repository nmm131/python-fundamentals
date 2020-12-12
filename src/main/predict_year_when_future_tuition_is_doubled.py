def predict_year_when_future_tuition_is_doubled(tuition, tuition_increase_percentage):
    count = 0
    total_tuition = tuition
    tuition_doubled = tuition * 2
    while True:
        count += 1
        total_tuition = total_tuition + total_tuition * tuition_increase_percentage/100
        if total_tuition >= tuition_doubled:
            break
    return count
