import requests
from PIL import Image
from io import BytesIO

API = "https://api.thecatapi.com/v1"


def get_random_cat_image():
    # Выполняем GET-запрос к API
    response: requests.Response = requests.get(f"{API}/images/search")

    if response.status_code == 200:  # Проверяем, успешен ли запрос
        # Преобразуем ответ в формате JSON в словарь
        data = response.json()
        # Извлекаем URL изображения из данных
        image_url = data[0]["url"]
        # Возвращаем URL изображения
        return image_url
    else:  # Если запрос не успешен
        # Выбрасываем исключение с сообщением об ошибке
        raise Exception(f"Ошибка при получении данных от The Cat API: {response.status_code}"
        )


def display_image(image_url: str) -> None:
    # Выполняем GET-запрос для получения изображения
    response = requests.get(image_url)

    # Проверяем, успешен ли запрос
    if response.status_code == 200:
        # Извлекаем содержимое ответа (данные изображения)
        img_data = response.content
        # Открываем изображение из байтового потока
        img = Image.open(BytesIO(img_data))
        # Показываем изображение
        img.show()
    else:  # Если запрос не успешен
        # Выбрасываем исключение с сообщением об ошибке
        raise Exception(
            f"Ошибка при получении изображения с {image_url}: {response.status_code}")


def main() -> None:
    # Получаем URL случайного изображения кота
    image_url = get_random_cat_image()
    # Печатаем URL изображения
    print(f"URL изображения кота: {image_url}")
    # Отображаем изображение
    display_image(image_url)


if __name__ == "__main__":
    main()
