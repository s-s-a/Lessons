# import requests
import niquests as requests


def download_image(url, filename):
    try:
        # Отправляем GET-запрос по указанному URL
        response = requests.get(url, stream=True)
        # Проверяем, что запрос был успешным (статус 200)
        response.raise_for_status()

        # Открываем файл в бинарном режиме записи ('wb')
        with open(filename, 'wb') as file:
            # Записываем содержимое ответа в файл
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Изображение успешно сохранено как: {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при скачивании изображения: {e}")
    except IOError as e:
        print(f"Ошибка при сохранении файла: {e}")


# Пример использования функции
if __name__ == "__main__":
    image_url = "https://placehold.co/600x400/000000/FFFFFF?text=Пример+изображения"  # Замените на реальный URL изображения
    output_filename = "saved_image.jpg"  # Имя файла для сохранения

    download_image(image_url, output_filename)
