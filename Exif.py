""" Работа с EXIF """
# https://habr.com/ru/company/skillfactory/blog/551002/

from exif import Image
import reverse_geocoder as rg
import pycountry


def format_dms_coordinates(coordinates) -> str:
    return f"{coordinates[0]}° {coordinates[1]}\' {coordinates[2]}\""


def dms_coordinates_to_dd_coordinates(coordinates, coordinates_ref) -> str:
    decimal_degrees = coordinates[0] + \
                      coordinates[1] / 60 + \
                      coordinates[2] / 3600

    if coordinates_ref == "S" or coordinates_ref == "W":
        decimal_degrees = -decimal_degrees

    return decimal_degrees


def draw_map_for_location(latitude, latitude_ref, longitude, longitude_ref):
    import webbrowser

    decimal_latitude = dms_coordinates_to_dd_coordinates(latitude, latitude_ref)
    decimal_longitude = dms_coordinates_to_dd_coordinates(longitude, longitude_ref)
    url = f"https://www.google.com/maps?q={decimal_latitude},{decimal_longitude}"
    webbrowser.open_new_tab(url)


def degrees_to_direction(degrees) -> str:
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
        "NNW"
    ]

    compass_directions_count = len(compass_directions)
    compass_direction_arc = 360 / compass_directions_count
    return compass_directions[int(degrees / compass_direction_arc) % compass_directions_count]


def format_direction_ref(direction_ref) -> str:
    direction_ref_text = "(true or magnetic north not specified)"
    if direction_ref == "T":
        direction_ref_text = "True north"
    elif direction_ref == "M":
        direction_ref_text = "Magnetic north"
    return direction_ref_text


def format_altitude(altitude, altitude_ref) -> str:
    altitude_ref_text = "(above or below sea level not specified)"
    if altitude_ref == 0:
        altitude_ref_text = "above sea level"
    elif altitude_ref == 1:
        altitude_ref_text = "below sea level"
    return f"{altitude} meters {altitude_ref_text}"


def format_speed_ref(speed_ref) -> str:
    speed_ref_text = "(speed units not specified)"
    if speed_ref == "K":
        speed_ref_text = "km/h"
    elif speed_ref == "M":
        speed_ref_text = "mph"
    elif speed_ref == "N":
        speed_ref_text = "knots"
    return speed_ref_text


with open("./images/palm tree 1.jpg", "rb") as palm_1_file:
    palm_1_image = Image(palm_1_file)

with open("./images/palm tree 2.jpg", "rb") as palm_2_file:
    palm_2_image = Image(palm_2_file)

images = [palm_1_image, palm_2_image]

# проверка ниличия EXIF
for index, image in enumerate(images):
    if image.has_exif:
        status = f"contains EXIF (version {image.exif_version}) information."
    else:
        status = "does not contain any EXIF information."
    print(f"Image {index} {status}")

# image_members = []
#
# for image in images:
#     image_members.append(dir(image))

# Список всех тегов
for index, image_member_list in enumerate(images):
    print(f"Image {index} contains {len(image_member_list)} members:")
    print(f"{image_member_list}\n")

# Спсиок тегов, общих для всех файлов
common_members = set(images[0]).intersection(set(images[1]))
common_members_sorted = sorted(list(common_members))
print("Image 0 and Image 1 have these members in common:")
print(f"{common_members_sorted}")

# Модели устройств(камер)
for index, image in enumerate(images):
    print(f"Device information - Image {index}")
    print("----------------------------")
    print(f"Make: {image.make}")
    print(f"Model: {image.model}\n")

# Стекло(объектив) и ОС камеры
for index, image in enumerate(images):
    print(f"Lens and OS - Image {index}")
    print("---------------------")
    print(f"Lens make: {image.get('lens_make', 'Unknown')}")
    print(f"Lens model: {image.get('lens_model', 'Unknown')}")
    print(f"Lens specification: {image.get('lens_specification', 'Unknown')}")
    print(f"OS version: {image.get('software', 'Unknown')}\n")

# Дата и время создания снимка
for index, image in enumerate(images):
    print(f"Date/time taken - Image {index}")
    print("-------------------------")
    print(f"{image.datetime_original}.{image.subsec_time_original} {image.get('offset_time', '')}\n")

# GGPS координаты места съемки в виде кортежей
for index, image in enumerate(images):
    print(f"Coordinates - Image {index}")
    print("---------------------")
    print(f"Latitude: {image.gps_latitude} {image.gps_latitude_ref}")
    print(f"Longitude: {image.gps_longitude} {image.gps_longitude_ref}\n")

# GGPS координаты места съемки в виде град мин сек и десятичных градусах
for index, image in enumerate(images):
    print(f"Coordinates - Image {index}")
    print("---------------------")
    print(f"Latitude (DMS): {format_dms_coordinates(image.gps_latitude)} {image.gps_latitude_ref}")
    print(f"Longitude (DMS): {format_dms_coordinates(image.gps_longitude)} {image.gps_longitude_ref}\n")
    print(f"Latitude (DD): {dms_coordinates_to_dd_coordinates(image.gps_latitude, image.gps_latitude_ref)}")
    print(f"Longitude (DD): {dms_coordinates_to_dd_coordinates(image.gps_longitude, image.gps_longitude_ref)}\n")

# места съемок на карте
for index, image in enumerate(images):
    draw_map_for_location(image.gps_latitude,
                          image.gps_latitude_ref,
                          image.gps_longitude,
                          image.gps_longitude_ref)

for index, image in enumerate(images):
    print(f"Location info - Image {index}")
    print("-----------------------")
    decimal_latitude = dms_coordinates_to_dd_coordinates(image.gps_latitude, image.gps_latitude_ref)
    decimal_longitude = dms_coordinates_to_dd_coordinates(image.gps_longitude, image.gps_longitude_ref)
    coordinates = (decimal_latitude, decimal_longitude)
    location_info = rg.search(coordinates)[0]
    location_info['country'] = pycountry.countries.get(alpha_2=location_info['cc'])
    print(f"{location_info}\n")

# Display camera direction for each image (Направление взгляда)
for index, image in enumerate(images):
    print(f"Image direction - Image {index}")
    print("-------------------------")
    print(f"Image direction: {degrees_to_direction(image.gps_img_direction)} ({image.gps_img_direction}°)")
    print(f"Image direction ref: {format_direction_ref(image.gps_img_direction_ref)}\n")

# Высота над уровнем моря
for index, image in enumerate(images):
    print(f"Altitude - Image {index}")
    print("------------------")
    print(f"{format_altitude(image.gps_altitude, image.gps_altitude_ref)}\n")

for index, image in enumerate(images):
    print(f"Speed - Image {index}")
    print("---------------")
    print(f"Speed: {image.gps_speed} {format_speed_ref(image.gps_speed_ref)}\n")

# Запись в EXIF файла

with open(f"./images/hotel original.jpg", "rb") as hotel_file:
    hotel_image = Image(hotel_file)

# Read the GPS data
print("Original coordinates")
print("--------------------")
print(f"Latitude: {hotel_image.gps_latitude} {hotel_image.gps_latitude_ref}")
print(f"Longitude: {hotel_image.gps_longitude} {hotel_image.gps_longitude_ref}\n")

# Open a Google Map showing the location represented by these coordinates
draw_map_for_location(hotel_image.gps_latitude,
                      hotel_image.gps_latitude_ref,
                      hotel_image.gps_longitude,
                      hotel_image.gps_longitude_ref)

# Boring. Let's change those coordinates to Area 51!
hotel_image.gps_latitude = (37.0, 14, 3.6)
hotel_image.gps_latitude_ref = 'N'
hotel_image.gps_longitude = (115, 48, 23.99)
hotel_image.gps_longitude_ref = 'W'

# Read the revised GPS data
print("Revised coordinates")
print("-------------------")
print(f"Latitude: {hotel_image.gps_latitude} {hotel_image.gps_latitude_ref}")
print(f"Longitude: {hotel_image.gps_longitude} {hotel_image.gps_longitude_ref}\n")

# Open a Google Map showing the location represented by the revised coordinates
draw_map_for_location(hotel_image.gps_latitude,
                      hotel_image.gps_latitude_ref,
                      hotel_image.gps_longitude,
                      hotel_image.gps_longitude_ref)

hotel_image.image_description = "The Dolphin Hotel in Orlando, viewed at sunset from the Swan Hotel"
hotel_image.copyright = "Copyright 2021 (Your name here)"

print(f"Description: {hotel_image.image_description}")
print(f"Copyright: {hotel_image.copyright}")

# Варианты очистки данных в EXIF
hotel_image.delete('gps_latitude')
hotel_image.delete('gps_latitude_ref')

del hotel_image.gps_longitude
del hotel_image.gps_longitude_ref

hotel_image.delete_all()

# Запись с измененным содержимым
with open('./images/hotel updated.jpg', 'wb') as updated_hotel_file:
    updated_hotel_file.write(hotel_image.get_file())