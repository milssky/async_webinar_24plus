import time

def get_page():
    print("Starting to download page")
    time.sleep(1)  # имитация http запроса 
    print("Done downloading page")
    return "<html>Hello</html>"

def read_db():
    print("Starting to retrieve data from db")
    time.sleep(0.5) # имитация подключения к бд
    print("Connected to db")
    time.sleep(1)  # имитация чтения из бд данных
    print("Done retrieving data from db")
    return "db-data"


def run():
    start = time.time()
    get_page()
    read_db()
    print(f'Elapsed time: {time.time() - start}')

