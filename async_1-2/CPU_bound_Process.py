import time
from multiprocessing import Process


def countdown():
    i = 0
    while i < 5_000_000:
        i += 1

process_list = []

if __name__ == '__main__':
    start_time = time.time()

    for i in range(10):
        process = Process(target=countdown)
        process_list.append(process)
        process.start()

    for process in process_list:
        process.join()

    end_time = time.time()

    print(f'Время выполнения через процессы: {end_time - start_time} секунды')