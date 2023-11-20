#Decorator

from time import time

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'It took {t2 - t1} secs')
        return result
    return wrapper

@performance
def long_time():
    for i in range(100000000):
        i*7

long_time()