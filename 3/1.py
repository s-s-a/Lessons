import time

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def benchmark(limit):
    count = 0
    for i in range(limit):
        if is_prime(i):
            count += 1
    return count

if __name__ == "__main__":
    start = time.perf_counter()
    result = benchmark(10_000_000)
    end = time.perf_counter()

    print(f"Found {result} primes in {end - start:.2f} seconds")
