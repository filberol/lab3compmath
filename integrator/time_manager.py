import time
from terminal_colors import *


def time_count(func):
    def wrapper(*args, **kwargs):
        begin = round(time.time()*1000)
        result = func(*args, **kwargs)
        end = round(time.time()*1000)
        print_c(f"Time elapsed: {end - begin} ms", Colors.OKBLUE)
        return result
    return wrapper
