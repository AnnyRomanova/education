from multiprocessing import Process
import os

def get_change_value(increment: int):
    print(f"Process {os.getpid()} started")
    with open("values.txt", "r+") as file:
        value = int(file.read().strip())
    print(f"Value in file - {value}")

    new_value = value + increment
    print(f"New value - {new_value}")

    with open("values.txt", "w") as file:
        file.write(str(new_value))

    print(f"Process {os.getpid()} stop")

if __name__ == "__main__":
    print(f"Main process {os.getpid()} started")
    p1 = Process(target=get_change_value, args=(2,))
    p2 = Process(target=get_change_value, args=(5,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    with open("values.txt", "r") as f:
        final_value = f.read()

    print(f"Main process {os.getpid()} stop. Final_value - {final_value}")