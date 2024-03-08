from time import perf_counter


def check_time(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        func(*args, **kwargs)
        print(f'time: {(perf_counter() - start):.02f}')

    return wrapper
