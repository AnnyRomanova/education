import requests
import time
from multiprocessing import Process



def make_request():
    url = "https://api.covidtracking.com/v1/us/current.json"
    r = requests.get(url)
    return len(r.text)


if __name__ == '__main__':
    start_time = time.time()

    thread1 = Process(target=make_request, daemon=True)
    thread2 = Process(target=make_request, daemon=True)
    thread3 = Process(target=make_request, daemon=True)
    thread4 = Process(target=make_request, daemon=True)
    thread5 = Process(target=make_request, daemon=True)
    thread6 = Process(target=make_request, daemon=True)
    thread7 = Process(target=make_request, daemon=True)
    thread8 = Process(target=make_request, daemon=True)
    thread9 = Process(target=make_request, daemon=True)
    thread10 = Process(target=make_request, daemon=True)

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()
    thread9.start()
    thread10.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
    thread7.join()
    thread8.join()
    thread9.join()
    thread10.join()

    end_time = time.time()

    print(f'Время выполнения через процессы: {end_time - start_time} секунды')