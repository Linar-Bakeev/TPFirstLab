from functools import wraps


def cached(function):
    mem = {}

    @wraps(function)
    def wrapper(*args):
        try:
            return mem[args]
        except KeyError:
            rowv = function(*args)
        mem[args] = rowv
        return rowv

    return wrapper


@cached
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


print([fib(i) for i in range(10)])
