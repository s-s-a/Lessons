"""Работа с EXIF"""

import os
import shutil

import pycountry
import reverse_geocoder as rg
from exif import Image

# https://habr.com/ru/company/skillfactory/blog/551002/

SOURCE_TRANSFER_PATH = r"c:\Users\sssss\Images\Nikon Transfer 2"


def format_dms_coordinates(coordinates) -> str:
    """
    Форматирование координат в градусах, минутах и секундах
    :param coordinates:
    :return:
    """
    return f"{coordinates[0]}° {coordinates[1]}' {coordinates[2]}\""


def dms_coordinates_to_dd_coordinates(coordinates, coordinates_ref) -> str:
    """
    Преобразование координат в градусах, минутах и секундах в градусах десятичных
    :param coordinates:
    :param coordinates_ref:
    :return:
    """
    decimal_degrees = coordinates[0] + coordinates[1] / 60 + coordinates[2] / 3600

    if coordinates_ref == "S" or coordinates_ref == "W":
        decimal_degrees = -decimal_degrees

    return decimal_degrees


def degrees_to_direction(degrees) -> str:
    """
    Форматирование направления
    :param degrees:
    :return:
    """
    compass_directions = [
        "N",
        "NNE",
        "NE",
        "ENE",
        "E",
        "ESE",
        "SE",
        "SSE",
        "S",
        "SSW",
        "SW",
        "WSW",
        "W",
        "WNW",
        "NW",
        "NNW",
    ]

    compass_directions_count = len(compass_directions)
    compass_direction_arc = 360 / compass_directions_count
    return compass_directions[
        int(degrees / compass_direction_arc) % compass_directions_count
    ]


def format_direction_ref(direction_ref) -> str:
    """
    Форматирование указания на полюс
    :param direction_ref:
    :return:
    """
    direction_ref_text = "(true or magnetic north not specified)"
    if direction_ref == "T":
        direction_ref_text = "True north"
    elif direction_ref == "M":
        direction_ref_text = "Magnetic north"
    return direction_ref_text


def format_altitude(altitude, altitude_ref) -> str:
    """
    Форматирование высоты
    :param altitude:
    :param altitude_ref:
    :return:
    """
    altitude_ref_text = "(above or below sea level not specified)"
    if altitude_ref == 0:
        altitude_ref_text = "above sea level"
    elif altitude_ref == 1:
        altitude_ref_text = "below sea level"
    return f"{altitude} meters {altitude_ref_text}"


def format_speed_ref(speed_ref) -> str:
    """
    Форматирование скорости
    :param speed_ref:
    :return:
    """
    speed_ref_text = "(speed units not specified)"
    if speed_ref == "K":
        speed_ref_text = "km/h"
    elif speed_ref == "M":
        speed_ref_text = "mph"
    elif speed_ref == "N":
        speed_ref_text = "knots"
    return speed_ref_text


def main():
    """
    Переделка примера работы с EXIF в виде обработки множества файлов с перемещением файлов
    в зависимости от наличия информации о дате съёмки
    """
    # with open(input('[~] Введите путь к 1-му файлу: '), "rb") as palm_1_file:
    #     palm_1_image = Image(palm_1_file)
    #
    # with open(input('[~] Введите путь к 2-му файлу: '), "rb") as palm_2_file:
    #     palm_2_image = Image(palm_2_file)

    files = [
        f"{SOURCE_TRANSFER_PATH}\\{x}".lower()
        for x in os.listdir(SOURCE_TRANSFER_PATH)
        if x.lower().endswith(".jpg")
    ]
    if len(files) == 0:
        print(f"В папке {SOURCE_TRANSFER_PATH} не найдены файлы с информацией об EXIF")
        return

    # image_members = []

    for file in files:  # in enumerate(images):

        # проверка наличия EXIF
        image = Image(file)
        print(file)
        status = ""
        if image.has_exif:
            try:
                if hasattr(image, "exif_version"):
                    status = f"contains EXIF (version {image.exif_version}) information."
            except Exception as e:
                status = " no contains EXIF version information."
                print(f"Ошибка: {e}")
        else:
            status = "does not contain any EXIF information."
        
        print(f"Image {status}")

        # image_members.append(dir(image))

        # Список всех тегов
        print(f"Image contains {len(image.list_all())} members:")
        print(f"{image.list_all()}\n")

        # # Список тегов, общих для всех файлов
        # common_members = set(image.list_all()).intersection(set(images[1].list_all()))
        # common_members_sorted = sorted(common_members)
        # print("Image 0 and Image 1 have these members in common:")
        # print(f"{common_members_sorted}")

        # Модели устройств(камер)
        print("Device information ")
        print("----------------------------")
        print(f"Make: {image.make}")
        print(f"Model: {image.model}\n")

        # Стекло(объектив) и ОС камеры
        print("Lens and OS")
        print("---------------------")
        print(f"Lens make: {image.get('lens_make', 'Unknown')}")
        print(f"Lens model: {image.get('lens_model', 'Unknown')}")
        print(f"Lens specification: {image.get('lens_specification', 'Unknown')}")
        print(f"OS version: {image.get('software', 'Unknown')}\n")

        # Дата и время создания снимка
        print("Date/time taken")
        print("-------------------------")
        try:
            print(
                f"{image.datetime_original}.{image.subsec_time_original} {image.get('offset_time', '')}\n"
            )
        except AttributeError:
            print("Date/time is not available.\n")

        # GGPS координаты места съемки в виде кортежей
        print("Coordinates")
        print("---------------------")
        try:
            print(f"Latitude: {image.gps_latitude} {image.gps_latitude_ref}")
            print(f"Longitude: {image.gps_longitude} {image.gps_longitude_ref}\n")
        except AttributeError:
            print("Coordinates are not available.\n")

        # GGPS координаты места съемки в виде град мин сек и десятичных градусах
        print("Coordinates")
        print("---------------------")
        try:
            print(
                f"Latitude (DMS): {format_dms_coordinates(image.gps_latitude)} {image.gps_latitude_ref}"
            )
            print(
                f"Longitude (DMS): {format_dms_coordinates(image.gps_longitude)} {image.gps_longitude_ref}\n"
            )
            print(
                f"Latitude (DD): {dms_coordinates_to_dd_coordinates(image.gps_latitude, image.gps_latitude_ref)}"
            )
            print(
                f"Longitude (DD): {dms_coordinates_to_dd_coordinates(image.gps_longitude, image.gps_longitude_ref)}\n"
            )
        except AttributeError:
            print("Coordinates are not available.\n")

        # места съемок на карте
        # try:
        #     draw_map_for_location(
        #         image.gps_latitude,
        #         image.gps_latitude_ref,
        #         image.gps_longitude,
        #         image.gps_longitude_ref,
        #     )
        # except AttributeError:
        #     print("Coordinates are not available.\n")

        print("Location info")
        print("-----------------------")
        try:
            decimal_latitude = dms_coordinates_to_dd_coordinates(
                image.gps_latitude, image.gps_latitude_ref
            )
            decimal_longitude = dms_coordinates_to_dd_coordinates(
                image.gps_longitude, image.gps_longitude_ref
            )
            coordinates = (decimal_latitude, decimal_longitude)
            location_info = rg.search(coordinates, mode=1)[0]
            location_info["country"] = pycountry.countries.get(
                alpha_2=location_info["cc"]
            )
            # print(location_info)
        except AttributeError:
            print("Coordinates are not available.\n")

        # Display camera direction for each image (Направление взгляда)
        print("Image direction")
        print("-------------------------")
        try:
            print(
                f"Image direction: {degrees_to_direction(image.gps_img_direction)} ({image.gps_img_direction}°)"
            )
            print(
                f"Image direction ref: {format_direction_ref(image.gps_img_direction_ref)}\n"
            )
        except AttributeError:
            print("Image direction is not available.\n")

        # Высота над уровнем моря
        print("Altitude")
        print("------------------")
        try:
            print(f"{format_altitude(image.gps_altitude, image.gps_altitude_ref)}\n")
        except AttributeError:
            print("Altitude is not available.\n")

        print("Speed")
        print("---------------")
        try:
            print(f"Speed: {image.gps_speed} {format_speed_ref(image.gps_speed_ref)}\n")
        except AttributeError:
            print("Speed is not available.\n")

        destination_folder = (
            SOURCE_TRANSFER_PATH + "\\" + image.datetime_original[0:10].replace(":", "")
        )
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # Перенесите файл
        print(f"Copying file: {file} to: {destination_folder}")
        # shutil.copy2(file, destination_folder) # копирование с сохранением атрибутов
        shutil.move(file, destination_folder)


if __name__ == "__main__":
    main()
