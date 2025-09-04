import time

start = time.perf_counter()

total = 0
for i in range(1, 10000):
    for j in range(1, 10000):
        total += i + j

end = time.perf_counter()
print(f"Result: {end - start:.2f} sec")
