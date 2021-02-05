from time import perf_counter
from functools import wraps

def measure_perf(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t0 = perf_counter()
        result = func(*args, **kwargs)
        t1 = perf_counter()
        print("Process took:", t1-t0)
        return result
    return wrapper