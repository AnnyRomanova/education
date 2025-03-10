import asyncio

counter = 0

# TODO используя Semaphore избежать длительного сна
async def do_request():
    global counter

    counter += 1
    if counter > 5:
        await asyncio.sleep(10)
    await asyncio.sleep(0.1)
    counter -= 1


async def safe_request(semaphore):
    async with semaphore:
        return await do_request()


async def main():
    semaphore = asyncio.Semaphore(5)
    await asyncio.wait_for(
        asyncio.gather(*[safe_request(semaphore) for _ in range(10)]),
        timeout=1.2,
    )
    print("Done")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())