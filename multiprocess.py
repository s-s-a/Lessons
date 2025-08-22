import multiprocessing
import time
from random import randint


def countUp():
    i = 0
    while i <= 3:
        print(f'Up:\t{i}')
        time.sleep(randint(1, 3))  # sleep 1, 2 or 3 seconds
        i += 1


def countDown():
    i = 3
    while i >= 0:
        print(f'Down:\t{i}')
        time.sleep(randint(1, 3))  # sleep 1, 2 or 3 seconds
        i -= 1


if __name__ == '__main__':
    # Initiate the workers.
    workerUp = multiprocessing.Process(target=countUp)
    workerDown = multiprocessing.Process(target=countDown)
    # Start the workers.
    workerUp.start()
    workerDown.start()

    # Join the workers. This will block in the main (parent) process
    # until the workers are complete.
    workerUp.join()
    workerDown.join()