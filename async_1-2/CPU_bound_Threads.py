import threading
import time


def countdown():
    i = 0
    while i < 5_000_000:
        i += 1


if __name__ == '__main__':
    start_time = time.time()

    thread1 = threading.Thread(target=countdown)
    thread2 = threading.Thread(target=countdown)
    thread3 = threading.Thread(target=countdown)
    thread4 = threading.Thread(target=countdown)
    thread5 = threading.Thread(target=countdown)
    thread6 = threading.Thread(target=countdown)
    thread7 = threading.Thread(target=countdown)
    thread8 = threading.Thread(target=countdown)
    thread9 = threading.Thread(target=countdown)
    thread10 = threading.Thread(target=countdown)

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

    print(f'Время выполнения через потоки: {end_time - start_time} секунды')