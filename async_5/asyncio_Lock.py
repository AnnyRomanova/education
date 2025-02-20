import asyncio
from asyncio import Lock

counter = 0
lock = Lock()

# TODO используя asyncio.Lock не допустить длительного сна
# убирать sleep() или изменять время сна нельзя

async def worker():
    global counter
    async with lock:
        await asyncio.sleep(0.1)
        counter += 1
        print(counter)
        if counter > 1:
            await asyncio.sleep(5)
        else:
            await asyncio.sleep(0.1)
        counter -= 1


res = "Успех"


async def main():
    global SUCCESS, res

    try:
        await asyncio.wait_for(
            asyncio.gather(*[worker() for _ in range(4)]), timeout=1
        )
    except asyncio.TimeoutError:
        res = "Долгое время выполнения!"

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print(res)