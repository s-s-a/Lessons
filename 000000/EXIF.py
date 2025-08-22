### EXIF
### https://habr.com/ru/company/skillfactory/blog/551002/
from exif import Image

def format_dms_coordinates(coordinates):
    return f"{coordinates[0]}° {coordinates[1]}\' {coordinates[2]}\""

def dms_coordinates_to_dd_coordinates(coordinates, coordinates_ref):
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


def degrees_to_direction(degrees):
    COMPASS_DIRECTIONS = [
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

    compass_directions_count = len(COMPASS_DIRECTIONS)
    compass_direction_arc = 360 / compass_directions_count
    return COMPASS_DIRECTIONS[int(degrees / compass_direction_arc) % compass_directions_count]

def format_direction_ref(direction_ref):
    direction_ref_text = "(true or magnetic north not specified)"
    if direction_ref == "T":
        direction_ref_text = "True north"
    elif direction_ref == "M":
        direction_ref_text = "Magnetic north"
    return direction_ref_text

def format_altitude(altitude, altitude_ref):
    altitude_ref_text = "(above or below sea level not specified)"
    if altitude_ref == 0:
        altitude_ref_text = "above sea level"
    elif altitude_ref == 1:
        altitude_ref_text = "below sea level"
    return f"{altitude} meters {altitude_ref_text}"

def format_speed_ref(speed_ref):
    speed_ref_text = "(speed units not specified)"
    if speed_ref == "K":
        speed_ref_text = "km/h"
    elif speed_ref == "M":
        speed_ref_text = "mph"
    elif speed_ref == "N":
        speed_ref_text = "knots"
    return speed_ref_text



with open("30_06_2015_15_36_03.JPEG", "rb") as palm_1_file:
    palm_1_image = Image(palm_1_file)

with open("Backofform.jpg", "rb") as palm_2_file:
    palm_2_image = Image(palm_2_file)

images = [palm_1_image, palm_2_image]


for index, image in enumerate(images):
    if image.has_exif:
        status = f"contains EXIF (version {image.exif_version}) information."
        print(f"Memeber list: {image.list_all()}")
        print(f"Tags & values list: {image.get_all()}")
    else:
        status = "does not contain any EXIF information."
    print(f"Image {index} {status}")



image_members = []

for image in images:
    image_members.append(dir(image))

for index, image_member_list in enumerate(image_members):
    print(f"Image {index} contains {len(image_member_list)} members:")
    print(f"{image_member_list}\n")


common_members = set(image_members[0]).intersection(set(image_members[1]))
common_members_sorted = sorted(list(common_members))
print("Image 0 and Image 1 have these members in common:")
print(f"{common_members_sorted}")


for index, image in enumerate(images):
    print(f"Device information - Image {index}")
    print("----------------------------")
    if image.has_exif:
      print(f"Make: {image.get('make', 'Unknown')}")
      print(f"Model: {image.get('model', 'Unknown')}\n")


for index, image in enumerate(images):
    print(f"Lens and OS - Image {index}")
    print("---------------------")
    if image.has_exif:
      print(f"Lens make: {image.get('lens_make', 'Unknown')}")
      print(f"Lens model: {image.get('lens_model', 'Unknown')}")
      print(f"Lens specification: {image.get('lens_specification', 'Unknown')}")
      print(f"OS version: {image.get('software', 'Unknown')}\n")


for index, image in enumerate(images):
    print(f"Date/time taken - Image {index}")
    print("-------------------------")
    if image.has_exif:
      print(f"{image.datetime_original}.{image.subsec_time_original} {image.get('offset_time', '')}\n")


for index, image in enumerate(images):
    print(f"Coordinates - Image {index}")
    print("---------------------")
    if image.has_exif:
      print(f"Latitude: {image.gps_latitude} {image.gps_latitude_ref}")
      print(f"Longitude: {image.gps_longitude} {image.gps_longitude_ref}\n")

for index, image in enumerate(images):
    print(f"Coordinates - Image {index}")
    print("---------------------")
    if image.has_exif:
      print(f"Latitude (DMS): {format_dms_coordinates(image.gps_latitude)} {image.gps_latitude_ref}")
      print(f"Longitude (DMS): {format_dms_coordinates(image.gps_longitude)} {image.gps_longitude_ref}\n")
      print(f"Latitude (DD): {dms_coordinates_to_dd_coordinates(image.gps_latitude, image.gps_latitude_ref)}")
      print(f"Longitude (DD): {dms_coordinates_to_dd_coordinates(image.gps_longitude, image.gps_longitude_ref)}\n")


for index, image in enumerate(images):
    if image.has_exif:
      draw_map_for_location(image.gps_latitude,
                            image.gps_latitude_ref,
                            image.gps_longitude,
                            image.gps_longitude_ref)

'''
import reverse_geocoder as rg
import pycountry

for index, image in enumerate(images):
    print(f"Location info - Image {index}")
    print("-----------------------")
    decimal_latitude = dms_coordinates_to_dd_coordinates(image.gps_latitude, image.gps_latitude_ref)
    decimal_longitude = dms_coordinates_to_dd_coordinates(image.gps_longitude, image.gps_longitude_ref)
    coordinates = (decimal_latitude, decimal_longitude)
    location_info = rg.search(coordinates)[0]
    location_info['country'] = pycountry.countries.get(alpha_2=location_info['cc'])
    print(f"{location_info}\n")
'''

for index, image in enumerate(images):
    print(f"Image direction - Image {index}")
    print("-------------------------")
    if image.has_exif:
      print(f"Image direction: {degrees_to_direction(image.get('gps_img_direction', 0))} ({image.get('gps_img_direction', 0)}°)")
      print(f"Image direction ref: {format_direction_ref(image.get('gps_img_direction_ref', 'N/A'))}\n")

# Display camera altitude for each image
for index, image in enumerate(images):
    print(f"Altitude - Image {index}")
    print( "------------------")
    if image.has_exif:
      print(f"{format_altitude(image.gps_altitude, image.gps_altitude_ref)}\n")

for index, image in enumerate(images):
    print(f"Speed - Image {index}")
    print("---------------")
    if image.has_exif:
      print(f"Speed: {image.get('gps_speed')} {format_speed_ref(image.get('gps_speed_ref'))}\n")