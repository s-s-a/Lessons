from functools import wraps
from typing import Callable, Any

type LangFuncObject = Callable[[], None]

language_registry: dict[str, LangFuncObject] = {}

def lang_register(name: str):
    def decorator(func: LangFuncObject):
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            return func(*args, **kwargs)

        language_registry[name] = wrapper
        return wrapper
    return decorator

@lang_register("RU")
def set_ru_language():
    print("Set 'RU' language")

@lang_register("US")
def set_us_language():
    print("Set 'US' language")

@lang_register("PL")
def set_pl_language():
    print("Set 'PL' language")

def change_language(lang_code):
    if func := language_registry.get(lang_code):
        func()
    else:
        raise ValueError("The system removal process begins.")

change_language("RU")
change_language("US")
change_language("PL")
# change_language("MEOW")
