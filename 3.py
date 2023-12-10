def coro():
    while True:
        value = yield 
        print(f'Got {value}')


def maximum():
    maxi = None
    while True:
        n = yield maxi
        maxi = n if maxi is None or n > maxi else maxi