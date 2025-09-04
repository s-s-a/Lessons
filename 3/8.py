import hashlib
import itertools
import string
import time

def brute_md5(target_hash: str, max_length: int = 8):
    chars = string.ascii_lowercase + string.digits

    for length in range(1, max_length + 1):
        for combo in itertools.product(chars, repeat=length):
            attempt = ''.join(combo)
            # print(attempt)
            if hashlib.md5(attempt.encode()).hexdigest() == target_hash:
                return attempt
    return None

if __name__ == "__main__":
    password = "ctwek"
    hashed = hashlib.md5(password.encode()).hexdigest()

    print(f"Target hash: {hashed}")
    start = time.time()
    result = brute_md5(hashed, max_length=8)
    end = time.time()

    if result:
        print(f"Password found: {result}")
    else:
        print("Password not found")

    print(f"Time: {end - start:.2f} sec")
