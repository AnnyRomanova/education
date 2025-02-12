import threading
import time


def countdown():
    i = 0
    while i < 5_000_000:
        i += 1

thread_list = []

if __name__ == '__main__':
    start_time = time.time()

    for i in range(10):
        thread = threading.Thread(target=countdown)
        thread_list.append(thread)
        thread.start()

    for thread in thread_list:
        thread.join()

    end_time = time.time()

    print(f'Время выполнения через потоки: {end_time - start_time} секунды')