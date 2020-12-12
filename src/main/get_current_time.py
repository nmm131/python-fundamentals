import time


def get_current_time():
    current_time = time.time()
    hours = int(current_time // 3600 % 24)
    minutes = int(current_time // 60 % 60)
    seconds = int(current_time % 60)
    return hours, minutes, seconds
