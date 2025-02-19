import asyncio
import time
import aiohttp

url_list = ["https://httpbin.org/json",
            "https://httpbin.org/xml",
            "https://httpbin.org/html",
            "https://httpbin.org/encoding/utf8",
            "https://httpbin.org/ip",
            "https://httpbin.org/get"]


async def async_http(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(response.status)


async def main():
    await asyncio.gather(*(async_http(url) for url in url_list))


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f"Время выполнения через asyncio {end - start}")
