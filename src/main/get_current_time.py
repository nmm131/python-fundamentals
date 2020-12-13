import time


def get_current_time():
    current_time = time.time()
    remaining_seconds = current_time % 86400
    hours_in_EDT = int(remaining_seconds // 3600 - 5)
    minutes = int(current_time // 60 % 60)
    seconds = int(current_time % 60)
    return hours_in_EDT, minutes, seconds
