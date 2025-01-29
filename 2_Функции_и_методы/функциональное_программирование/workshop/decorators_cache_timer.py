def cache(func):
    results = {}
    def inner(*args):
        if args in results:
            return results[args]
        result = func(*args)
        results[args] = result
        return result

    return inner

import time

def time_it(func):
    def wrapper(*args, **kwargs):
        _start_time = time.time()
        _result = func(*args, **kwargs)
        _end_time = time.time()
        print(f"Function {func.__name__} took {_end_time - _start_time} seconds to run")
        return _result
    return wrapper


@time_it
def fib_hider(_n, cached : bool = False):
    if cached:
        return fib_cache(_n)
    else:
        return fib(_n)


@cache
def fib_cache(_n):
    if _n <= 1:
        return _n
    return fib_cache(_n - 1) + fib_cache(_n - 2)

def fib(_n):
    if _n <= 1:
        return _n
    return fib(_n - 1) + fib(_n - 2)

n = 35
print(fib_hider(n, False))
print(fib_hider(n,True))