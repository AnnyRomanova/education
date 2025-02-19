import threading
import time
import requests

url_list = ["https://httpbin.org/json",
            "https://httpbin.org/xml",
            "https://httpbin.org/html",
            "https://httpbin.org/encoding/utf8",
            "https://httpbin.org/ip",
            "https://httpbin.org/get"]


def request_threads(url):
    response = requests.get(url)
    print(response.status_code)


if __name__ == "__main__":

    start = time.time()

    thread_list = []
    for url in url_list:
        thread = threading.Thread(target=request_threads, args=(url,))
        thread_list.append(thread)
        thread.start()

    for thread in thread_list:
        thread.join()

    end = time.time()

print(f'Время выполнения через requests и потоки: {end - start}')
