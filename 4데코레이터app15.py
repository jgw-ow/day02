import time


def decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("실행시간 : {}".format(end - start))
    return wrapper

@decorator
def check_loop(cnt):
    for i in range(cnt):
        print('A', end='')
        
check_loop(1000000)
 
