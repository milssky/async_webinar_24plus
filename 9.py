import asyncio
from asyncio import sleep

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


async def worker():
    page = await get_page()
    await write_db(page)

async def call_gather():
    await asyncio.gather(worker(), worker(), worker())