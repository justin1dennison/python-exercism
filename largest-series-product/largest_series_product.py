from itertools import islice
from functools import reduce
from operator import mul

def identity(x):
    return x

def windowed(iterable, size):
    for i in range(len(iterable)):
        chunk = tuple(islice(iterable, i, i + size))
        if len(chunk) == size:
            yield chunk

def windowed_with(iterable, size, fn=identity):
    return (map(fn, window) for window in windowed(iterable, size))

def largest_product(series, size):
    if size == 0:
        return 1
    if not series:
        raise ValueError("Series must not be empty")
    if len(series) < size:
        raise ValueError("Size cannot be larger than size of series")
    if not series.isdecimal():
        raise ValueError("Series can only contain digits 0-9")
    return max(reduce(mul, window, 1) for window in windowed_with(series, size, int))

if __name__ == '__main__':
    print(largest_product('99099', 3))
