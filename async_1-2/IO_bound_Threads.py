import requests
import time
import threading



def make_request():
    url = "https://api.covidtracking.com/v1/us/current.json"
    r = requests.get(url)
    return len(r.text)

thread_list = []

if __name__ == '__main__':
    start_time = time.time()

    for i in range(10):
        thread = threading.Thread(target=make_request)
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()
        thread.join()

    end_time = time.time()

    print(f'Время выполнения через потоки: {end_time - start_time} секунды')