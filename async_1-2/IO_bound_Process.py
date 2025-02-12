import requests
import time
from multiprocessing import Process



def make_request():
    url = "https://api.covidtracking.com/v1/us/current.json"
    r = requests.get(url)
    return len(r.text)

process_list = []

if __name__ == '__main__':
    start_time = time.time()

    for i in range(10):
        process = Process(target=make_request)
        process_list.append(process)
        process.start()

    for process in process_list:
        process.join()

    end_time = time.time()

    print(f'Время выполнения через процессы: {end_time - start_time} секунды')
