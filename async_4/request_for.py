import time
import requests

url_list = ["https://httpbin.org/json",
            "https://httpbin.org/xml",
            "https://httpbin.org/html",
            "https://httpbin.org/encoding/utf8",
            "https://httpbin.org/ip",
            "https://httpbin.org/get"]


def request_for(list_url):
    start = time.time()
    for url in list_url:
        response = requests.get(url)
        print(response.status_code)
    print(f'Время выполнения через requests: {time.time() - start}')


if __name__ == "__main__":
    request_for(url_list)
