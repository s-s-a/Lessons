'''
Data Types
Note

All data types are constructed using the plum (pack/unpack memory) package.

Flash
classexif.Flash(*, flash_fired: bool, flash_return: FlashReturn, flash_mode: FlashMode, flash_function_not_present: bool, red_eye_reduction_supported: bool, reserved: int)
Status of the camera’s flash when the image was taken. (Reported by the flash tag.)

classexif.FlashMode
Flash mode of the camera.

classexif.FlashReturn
Flash status of returned light.

Enumerations
ColorSpace
classexif.ColorSpace
Color space specifier.

SRGB= 1
sRBG

UNCALIBRATED= 65535
Uncalibrated or Other

ExposureMode
classexif.ExposureMode
Exposure mode set when the image was shot.

AUTO_BRACKET= 2
Auto Bracket

AUTO_EXPOSURE= 0
Auto Exposure

MANUAL_EXPOSURE= 1
Manual Exposure

ExposureProgram
classexif.ExposureProgram
Class of the program used by the camera to set exposure when the picture is taken.

ACTION_PROGRAM= 6
Action Program (Biased Toward Fast Shutter Speed)

APERTURE_PRIORITY= 3
Aperture Priority

CREATIVE_PROGRAM= 5
Creative Program (Biased Toward Depth of Field)

LANDSCAPE_MODE= 8
Landscape Kode (For Landscape Photos with the Background in Focus)

MANUAL= 1
Manual

NORMAL_PROGRAM= 2
Normal Program

NOT_DEFINED= 0
Not Defined

PORTRAIT_MODE= 7
Portrait Mode (For Closeup Photos with the Background out of Focus)

SHUTTER_PRIORITY= 4
Shutter Priority

GpsAltitudeRef
classexif.GpsAltitudeRef
Altitude used as the reference altitude.

ABOVE_SEA_LEVEL= 0
Above Sea Level

BELOW_SEA_LEVEL= 1
Below Sea Level

LightSource
classexif.LightSource
Class of the program used by the camera to set exposure when the picture is taken.

CLOUDY_WEATHER= 10
Cloudy Weather

COOL_WHITE_FLUORESCENT= 14
Cool White Fluorescent (W 3900 - 4500K)

D50= 23
D50

D55= 20
D55

D65= 21
D65

D75= 22
D75

DAYLIGHT= 1
Daylight

DAYLIGHT_FLUORESCENT= 12
Daylight Fluorescent (D 5700 - 7100K)

DAY_WHITE_FLUORESCENT= 13
Day White Fluorescent (N 4600 - 5400K)

FINE_WEATHER= 9
Fine Weather

FLASH= 4
Flash

FLUORESCENT= 2
Fluorescent

ISO_STUDIO_TUNGSTEN= 24
ISO Studio Tungsten

OTHER= 255
Other Light Source

SHADE= 11
Shade

STANDARD_LIGHT_A= 17
Standard Light A

STANDARD_LIGHT_B= 18
Standard Light B

STANDARD_LIGHT_C= 19
Standard Light C

TUNGSTEN= 3
Tungsten (Incandescent Light)

UNKNOWN= 0
Unknown

WHITE_FLUORESCENT= 15
White Fluorescent (WW 3200 - 3700K)

MeteringMode
classexif.MeteringMode
Metering mode.

AVERAGE= 1
Average

CENTER_WEIGHTED_AVERAGE= 2
Center Weighted Average

MULTI_SPOT= 4
Multi Spot

OTHER= 255
Other

PARTIAL= 6
Partial

PATTERN= 5
Pattern

SPOT= 3
Spot

UNKNOWN= 0
Unknown

Orientation
classexif.Orientation
Image orientation in terms of rows and columns.

BOTTOM_LEFT= 4
The 0th row is at the visual bottom of the image and the 0th column is the visual left-hand side.

BOTTOM_RIGHT= 3
The 0th row is at the visual bottom of the image and the 0th column is the visual right-hand side.

LEFT_BOTTOM= 8
The 0th row is the visual left-hand side of the image and the 0th column is the visual bottom.

LEFT_TOP= 5
The 0th row is the visual left-hand side of the image and the 0th column is the visual top.

RIGHT_BOTTOM= 7
The 0th row is the visual right-hand side of the image and the 0th column is the visual bottom.

RIGHT_TOP= 6
The 0th row is the visual right-hand side of the image and the 0th column is the visual bottom.

TOP_LEFT= 1
The 0th row is at the visual top of the image and the 0th column is the visual left-hand side.

TOP_RIGHT= 2
The 0th row is at the visual top of the image and the 0th column is the visual right-hand side.

ResolutionUnit
classexif.ResolutionUnit
Unit for measuring X resolution and Y resolution tags.

CENTIMETERS= 3
Centimeters

INCHES= 2
Inches or Unknown

Saturation
classexif.Saturation
Saturation processing applied by camera.

HIGH= 2
High Saturation

LOW= 1
Low Saturation

NORMAL= 0
Normal Saturation

SceneCaptureType
classexif.SceneCaptureType
Type of scene that was shot or the mode in which the image was shot.

LANDSCAPE= 1
Landscape

NIGHT_SCENE= 3
Night Scene

PORTRAIT= 2
Portrait

STANDARD= 0
Standard

SensingMethod
classexif.SensingMethod
Image sensor type on the camera or input device.

COLOR_SEQUENTIAL_AREA_SENSOR= 5
Color Sequential Area Sensor

COLOR_SEQUENTIAL_LINEAR_SENSOR= 8
Color Sequential Linear Sensor

NOT_DEFINED= 1
Not Defined

ONE_CHIP_COLOR_AREA_SENSOR= 2
One-Chip Color Area Sensor

THREE_CHIP_COLOR_AREA_SENSOR= 4
Three-Chip Color Area Sensor

TRILINEAR_SENSOR= 7
Trilinear Sensor

TWO_CHIP_COLOR_AREA_SENSOR= 3
Two-Chip Color Area Sensor

Sharpness
classexif.Sharpness
Sharpness processing applied by camera.

HARD= 2
Hard

NORMAL= 0
Normal

SOFT= 1
Soft

WhiteBalance
classexif.WhiteBalance
White balance mode set when the image was shot.

AUTO= 0
Auto White Balance

MANUAL= 1
Manual White Balance

Image Attributes
The exif.Image interface provides access to the following EXIF tags as Python attributes:

acceleration
aperture_value
artist
bits_per_sample
body_serial_number
brightness_value
camera_elevation_angle
camera_owner_name
cfa_pattern
color_space
components_configuration
compressed_bits_per_pixel
compression
contrast
copyright
custom_rendered
datetime
datetime_digitized
datetime_original
device_setting_description
digital_zoom_ratio
exif_version
exposure_bias_value
exposure_index
exposure_mode
exposure_program
exposure_time
f_number
file_source
flash
flash_energy
flashpix_version
focal_length
focal_length_in_35mm_film
focal_plane_resolution_unit
focal_plane_x_resolution
focal_plane_y_resolution
gain_control
gamma
gps_altitude
gps_altitude_ref
gps_area_information
gps_datestamp
gps_dest_bearing
gps_dest_bearing_ref
gps_dest_distance
gps_dest_distance_ref
gps_dest_latitude
gps_dest_latitude_ref
gps_dest_longitude
gps_dest_longitude_ref
gps_differential
gps_dop
gps_horizontal_positioning_error
gps_img_direction
gps_img_direction_ref
gps_latitude
gps_latitude_ref
gps_longitude
gps_longitude_ref
gps_map_datum
gps_measure_mode
gps_processing_method
gps_satellites
gps_speed
gps_speed_ref
gps_status
gps_timestamp
gps_track
gps_track_ref
gps_version_id
humidity
image_description
image_height
image_unique_id
image_width
iso_speed
iso_speed_latitude_yyy
iso_speed_latitude_zzz
jpeg_interchange_format
jpeg_interchange_format_length
lens_make
lens_model
lens_serial_number
lens_specification
light_source
make
maker_note
matrix_coefficients
max_aperture_value
metering_mode
model
oecf
offset_time
offset_time_digitized
offset_time_original
orientation
photographic_sensitivity
photometric_interpretation
pixel_x_dimension
pixel_y_dimension
planar_configuration
pressure
primary_chromaticities
recommended_exposure_index
reference_black_white
related_sound_file
resolution_unit
rows_per_strip
samples_per_pixel
saturation
scene_capture_type
scene_type
sensing_method
sensitivity_type
sharpness
shutter_speed_value
software
spatial_frequency_response
spectral_sensitivity
standard_output_sensitivity
strip_byte_counts
strip_offsets
subject_area
subject_distance
subject_distance_range
subject_location
subsampling_ratio_of_y_to_c
subsec_time
subsec_time_digitized
subsec_time_original
temperature
transfer_function
user_comment
water_depth
white_balance
white_point
x_resolution
xp_author
xp_comment
xp_keywords
xp_subject
xp_title
y_and_c_positioning
y_resolution
'''
