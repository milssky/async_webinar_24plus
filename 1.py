"""Генераторы."""

# 1 1 2 3 5 8 13 ...

def fib_list(n):
    a, b = 1, 1
    numbers = []
    for _ in range(n):
        numbers.append(a)
        a, b = b, a + b
    return numbers

def fib_gen(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def indefinite():
    n = 0
    while True:
        yield n
        n += 1
