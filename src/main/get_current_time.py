import time


def get_current_time():
    current_time = time.time()
    hours = int(current_time % (24 * 3600) // 3600)
    minutes = int(current_time // 60 % 60)
    seconds = int(current_time % 60)
    return hours, minutes, seconds


#print(get_current_time())
