import hashlib
import time
import string

CHARS = string.ascii_lowercase + string.digits

def brute_md5(target_hash, max_length):
    def backtrack(current):
        if len(current) > max_length:
            return None
        guess = ''.join(current)
        # print(guess)

        if hashlib.md5(guess.encode()).hexdigest() == target_hash:
            return guess
        for ch in CHARS:
            result = backtrack(current + [ch])
            if result:
                return result
        return None

    return backtrack([])

if __name__ == "__main__":
    password = "qwerty12345"
    hashed = hashlib.md5(password.encode()).hexdigest()

    print(f"Target hash: {hashed}")
    start = time.time()
    result = brute_md5(hashed, max_length=4)
    end = time.time()

    if result:
        print(f"Password found: {result}")
    else:
        print("Password not found")

    print(f"Time: {end - start:.2f} seconds")
