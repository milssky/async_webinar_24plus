import time
import heapq
from collections import deque


class Sleep:
    def __init__(self, delay) -> None:
        self.delay = delay
    
    def __await__(self):
        yield ('sleep', self.delay)

def sleep(delay):
    return Sleep(delay)


async def get_page():
    print("Starting to download page")
    await sleep(1)  # имитация http запроса 
    print("Done downloading page")
    return "<html>Hello</html>"

async def write_db(data):
    print("Starting to retrieve data from db")
    await sleep(0.5) # имитация подключения к бд
    print("Connected to db")
    await sleep(1)  # имитация чтения из бд данных
    print("Done writing data to db")

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

def worker():
    page = yield from get_page()
    yield from write_db(page)