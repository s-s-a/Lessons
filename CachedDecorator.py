def cache(func) -> object:
    cache_calls = {}

    def wrapper(*args, **kwargs) -> object:
        tuple_args = args + tuple(kwargs.items())
        if tuple_args in cache_calls:
            return cache_calls[tuple_args]
        result = func(*args, **kwargs)
        cache_calls[tuple_args] = result
        return result

    return wrapper


@cache
def sum_all(a: int = 1, b: int = 2, c: int = 3) -> int:
    for i in range(10_000_000):
        i += a + b + c
    return i  # type: ignore


print('Start!')
print(sum_all(10, c=30))  # type: ignore
print('Stop!')
print(sum_all(10, c=30))  # type: ignore
print('Stop!')
print(sum_all(10, c=30))  # type: ignore
print('Stop!')
print(sum_all(10, c=30))  # type: ignore
print('Stop!')
print(sum_all(10, c=30))  # type: ignore
print('Stop!')
print(sum_all(10, c=30))  # type: ignore
print('Stop!')
print(sum_all(10, 5, c=30))  # type: ignore
print(sum_all(10, 5, c=30))  # type: ignore
print(sum_all(10, 5, c=30))  # type: ignore
print(sum_all(10, 5, c=30))  # type: ignore
print(sum_all(10, 5, c=30))  # type: ignore