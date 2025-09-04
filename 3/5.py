import threading
import time

def cpu_task(n):
    result = 1
    for i in range(1, n):
        result *= i
    return result

def worker(n, count):
    for _ in range(count):
        cpu_task(n)

def benchmark():
    threads = []
    start = time.time()
    for _ in range(5):
        t = threading.Thread(target=worker, args=(1_000, 100_000))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
    end = time.time()
    print(f"Result: {end - start:.2f} seconds")

if __name__ == "__main__":
    benchmark()
