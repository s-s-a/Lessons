# Код для сканирования открытых вкладок в Google Chrome на Python

# Как использовать:
# ✅ Запустить Chrome с отладочным портом: chrome.exe --remote-debugging-port=9222
# ✅Запустиnm скрипт — он выведет список всех открытых вкладок (название + URL).

import requests


def get_chrome_tabs(debug_port=9222):
    """
    Получает и выводит список открытых вкладок Chrome через удаленную отладку.

    Args:
        debug_port (int): Порт, на котором включена удаленная отладка.
                          По умолчанию используется порт 9222.
    """
    try:
        response = requests.get(f"http://localhost:{debug_port}/json")
        tabs = response.json()

        if not tabs:
            print("Нет открытых вкладок или отладка не включена.")
            return

        for i, tab in enumerate(tabs, start=1):
            title = tab.get('title', 'Без названия')
            url = tab.get('url', 'Без URL')
            print(f"{i}. {title} — {url}")

    except requests.exceptions.ConnectionError:
        print(f"Не удалось подключиться к Chrome (порт {debug_port}).")
        print("Убедитесь, что Chrome запущен с ключом: chrome.exe --remote-debugging-port=9222")


if __name__ == "__main__":
    get_chrome_tabs()
