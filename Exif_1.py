# pip install Pillow ffmpeg-python

# https://codeby.net/threads/izvlekaem-metadannye-iz-foto-audio-i-video-fajlov-s-pomoschju-python.80200/?utm_referrer=https%3A%2F%2Fdzen.ru%2Fmedia%2Fid%2F5db7e91e9515ee00b34ade7f%2F643d7f0c7906327d863682cb

import os.path
from pprint import pprint

import ffmpeg
from PIL import Image, ExifTags

NIKON_TRANSFER_PATH = r"c:\Users\sssss\Images\Nikon Transfer 2"



def image_metadata(path_f):
    """

    :param path_f:
    """
    img = Image.open(path_f)
    info_dict = {
            "Имя файла": os.path.split(path_f)[1],
            "Разрешение изображения": img.size,
            "Высота изображения": img.height,
            "Ширина изображения": img.width,
            "Формат изображения": img.format,
            "Режим изображения": img.mode,
            "Анимированное изображение": getattr(img, "is_animated", False),
            "Кадров в изображении": getattr(img, "n_frames", 1)
        }
    try:
        exif = {ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS}

        print(f'\n[+] Метаданные фото: {os.path.split(path_f)[1]:27}\n')
        for info in exif:
            if info == 'GPSInfo':
                print(f'{info:27}: lat {exif[info][2]} {exif[info][1]} - long {exif[info][4]} {exif[info][3]}')
            else:
                if isinstance(exif[info], bytes):
                    try:
                        info_d = exif[info].decode()
                    except UnicodeDecodeError:
                        info_d = exif[info]
                    print(f'{info:25}: {info_d}')
                else:
                    print(f'{info:25}: {exif[info]}')
    except AttributeError:
        print(f'\n[+] Информация о фото: {os.path.split(path_f)[1]:27}\n')
        for k, v in info_dict.items():
            print(f"{k:27}: {v}")
        exit(0)


def vid_aud_matadata(patn_f):
    try:
        print(f'\n[+] Метаданные файла: {os.path.split(patn_f)[-1]}\n')
        pprint(ffmpeg.probe(patn_f)["streams"])
    except ffmpeg._run.Error:
        print('[-] Неподдерживаемый формат')


if __name__ == "__main__":
    # path_file = input('[~] Введите путь к файлу: ').lower()
    files = [NIKON_TRANSFER_PATH+"\\"+x.lower() for x in os.listdir(NIKON_TRANSFER_PATH) if x.lower().endswith(".jpg")]
    for path_file in files:
        if not os.path.exists(path_file):
            print('[-] Файла не существует')
        else:
            if path_file.endswith(".jpg"):
                image_metadata(path_file)
            elif path_file.endswith(".jpeg"):
                image_metadata(path_file)
            else:
                vid_aud_matadata(path_file)
