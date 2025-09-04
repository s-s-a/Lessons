import requests
import time

URL = "https://jsonplaceholder.typicode.com/posts/1"

def parse_json():
    pass

def benchmark(n: int):
    for _ in range(n):
        response = requests.get(URL)
        _ = response.json()

if __name__ == "__main__":
    start = time.time()
    benchmark(50)
    end = time.time()
    print(f"Result: {end - start:.2f} sec")
