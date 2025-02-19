import time
import requests

url_list = ["https://httpbin.org/json",
            "https://httpbin.org/xml",
            "https://httpbin.org/html",
            "https://httpbin.org/encoding/utf8",
            "https://httpbin.org/ip",
            "https://httpbin.org/get"]

start = time.time()

for url in url_list:
    response = requests.get(url)
    print(response.status_code)

print(f'Время выполнения через requests: {time.time() - start}')
