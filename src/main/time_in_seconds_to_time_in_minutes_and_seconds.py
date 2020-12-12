def time_in_seconds_to_time_in_minutes_and_seconds(time_in_seconds):
    minutes = time_in_seconds // 60
    seconds = time_in_seconds % 60
    return minutes, seconds
