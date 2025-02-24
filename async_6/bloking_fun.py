import asyncio
import datetime
import requests
from concurrent.futures import ThreadPoolExecutor


def blocking_task():
    print("Запущена блокирующая функция")
    requests.get('https://docs.python.org/3/')


async def async_thread_worker(event_loop):
    print("Запущен отдельный поток с блокирующей функцией")
    with ThreadPoolExecutor() as executor:
        await event_loop.run_in_executor(executor, blocking_task)


async def ticker():
    print("Запущена корутина ticker")
    while True:
        print(datetime.datetime.now())
        await asyncio.sleep(1)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(ticker())
    loop.create_task(async_thread_worker(loop))
    loop.run_forever()
