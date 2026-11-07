
import os

from PIL import ExifTags, Image

NIKON_TRANSFER_PATH = r"c:\Users\sssss\Images\Nikon Transfer 2"

path_f = NIKON_TRANSFER_PATH

files = [
    f"{NIKON_TRANSFER_PATH}\\{x}".lower()
    for x in os.listdir(NIKON_TRANSFER_PATH)
    if x.lower().endswith(".jpg")
]
if len(files) == 0:
    print(f"В папке {NIKON_TRANSFER_PATH} не найдены файлы с информацией об EXIF")
    # return
else:

    # image_members = []

    for file in files:  # in enumerate(images):

        # проверка наличия EXIF
        image = Image.open(file)

        # Собираем метаданные
        metadata = {
            "Формат": image.format,
            "Размер": f"{image.width}x{image.height}",
            "Режим": image.mode,
            # "File ID": file_id,
            # "Размер файла": f"{file.file_size} байт"
        }

        # Получаем EXIF данные, если они есть
        exif = image.getexif()
        if exif:
            # Добавляем основные EXIF данные
            exif_data = {}
            for tag_id in exif:
                tag = exif.get(tag_id)
                tag_name = ExifTags.TAGS.get(tag_id, tag_id)
                exif_data[tag_name] = tag
            metadata["EXIF"] = exif_data

        # Формируем текст ответа
        result = "📸 Метаданные фотографии:\n\n"
        for key, value in metadata.items():
            if key != "EXIF":
                result += f"• {key}: {value}\n"

        if "EXIF" in metadata:
            result += "\n📑 EXIF данные:\n"
            for key, value in metadata["EXIF"].items():
                result += f"• {key}: {value}\n"

        # return result
        print(result)
