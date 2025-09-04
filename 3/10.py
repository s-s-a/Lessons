import re
import time
from collections import defaultdict

def word_frequency(text: str) -> dict:
    freq = defaultdict(int)
    words = re.findall(r'\b\w+\b', text.lower())
    for word in words:
        freq[word] += 1
    return freq

def run_analysis(repeats=1000):
    with open("big_text.txt", encoding="utf-8") as f:
        text = f.read()

    for _ in range(repeats):
        word_frequency(text)

if __name__ == "__main__":
    start = time.time()
    run_analysis()
    end = time.time()
    print(f"Completed in {end - start:.2f} seconds")
