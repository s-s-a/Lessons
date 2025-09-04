import time
from multiprocessing import Pool

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes(limit):
    return sum(1 for i in range(limit) if is_prime(i))

def benchmark():
    limits = [2_000_000, 2_000_000, 2_000_000, 2_000_000]
    start = time.time()

    with Pool(processes=4) as pool:
        results = pool.map(count_primes, limits)
    
    end = time.time()
    print(f"Result: {end - start:.2f} sec")

if __name__ == "__main__":
    benchmark()
