import time
import heapq
from collections import deque

def get_page():
    print("Starting to download page")
    yield ('sleep', 1)  # имитация http запроса 
    print("Done downloading page")
    yield "<html>Hello</html>"

def read_db():
    print("Starting to retrieve data from db")
    yield ('sleep', 0.5) # имитация подключения к бд
    print("Connected to db")
    yield ('sleep', 1)  # имитация чтения из бд данных
    print("Done retrieving data from db")
    yield "db-data"


def scheduler(coros):
    start = time.time()
    ready = deque(coros)
    sleeping = []

    while True:
        if not ready and not sleeping:
            break

        if not ready:
            deadline, coro = heapq.heappop(sleeping)
            if deadline > time.time():
                time.sleep(deadline - time.time())
            ready.append(coro)
        
        try:
            coro = ready.popleft()
            result = coro.send(None)
            if len(result) == 2 and result[0] == 'sleep':
                deadline = time.time() + result[1]
                heapq.heappush(sleeping, (deadline, coro))
            else:
                print(f'Got: {result}')
                ready.append(coro)
        except StopIteration:
            pass
    print(f'Elapsed time: {time.time() - start}')

