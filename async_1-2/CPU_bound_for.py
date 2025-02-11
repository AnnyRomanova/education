import time


def countdown():
    i = 0
    while i < 5_000_000:
        i += 1


if __name__ == '__main__':
    start_time = time.time()

    for i in range(10):
        countdown()

    end_time = time.time()

    print(f'Время выполнения через цикл for: {end_time - start_time} секунды')
