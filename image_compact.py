# Код для массового сжатия изображений в папке на Python

# Для массового сжатия изображений в коде используется библиотека Pillow, для добавления прогресс-бара - tqdm.

from pathlib import Path
from PIL import Image
from tqdm import tqdm


def process_images_compact(input_path: str, output_folder: str = 'out', max_width: int = 1920, quality: int = 85):
    out_dir = Path(output_folder)
    out_dir.mkdir(parents=True, exist_ok=True)

    allowed_exts = {'.jpg', '.jpeg', '.png'}

    # Собираем список всех файлов в input_path (и подпапках), которые имеют разрешенные расширения
    # rglob('*') рекурсивно ищет все файлы и папки
    files = [p for p in Path(input_path).rglob('*') if p.suffix.lower() in allowed_exts]

    for p in tqdm(files, leave=False):
        # Открываем изображение с помощью Pillow
        im = Image.open(p)
        # Получаем текущие ширину и высоту изображения
        w, h = im.size

        # Проверяем, превышает ли ширина изображения заданную максимальную ширину
        if w > max_width:
            # Вычисляем коэффициент масштабирования
            ratio = max_width / w
            # Изменяем размер изображения, сохраняя пропорции
            im = im.resize((max_width, int(h * ratio)))

        # Определяем полный путь для сохранения обработанного изображения в выходной папке
        output_file_path = out_dir / p.name

        # Сохраняем изображение
        if p.suffix.lower() == '.png':
            im.save(output_file_path, optimize=True)
        else:
            im.save(output_file_path, quality=quality, optimize=True)


if __name__ == "__main__":
    process_images_compact('my_photos', output_folder='resized_photos', max_width=1024, quality=80)
