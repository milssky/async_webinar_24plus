from collections import deque

def coro1():
    print("coro1 doing some work")
    yield
    print("coro1 doing some work")
    yield

def coro2():
    print("coro2 doing some work")
    yield
    print("coro2 doing some work")
    yield

# def scheduler():
#     c1 = coro1()
#     c2 = coro2()
#     c1.send(None)
#     c2.send(None)
#     c1.send(None)
#     c2.send(None)

def scheduler(coros: list):
    ready = deque(coros)
    while ready:
        try:
            coro = ready.popleft()
            result = coro.send(None)
            ready.append(coro)
        except StopIteration:
            pass

