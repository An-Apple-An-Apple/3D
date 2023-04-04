# https://www.geogebra.org/calculator/ghwysc7z Geogebra representation
# I know the documentations are horrible, working on it...
# Gavin 2022
# This version is made scratch-friendly with more hard coded variables but easier to implement in scratch

import math


# polar
def find_polar_x_change(z_rotation):
    return round(math.sin(math.radians(z_rotation)), ndigits=4) * camera_x_y_magnitude


def find_polar_y_change(z_rotation):
    return round(math.cos(math.radians(z_rotation)), ndigits=4) * camera_x_y_magnitude


def find_polar_z_change(up_down_rotation):
    return round(math.sin(math.radians(up_down_rotation)), ndigits=4) * camera_y_z_magnitude


# return the vector
def polar_vector():
    global camera_x_change
    global camera_y_change
    global camera_z_change
    camera_x_change = find_polar_x_change(z_rotation)
    camera_y_change = find_polar_y_change(z_rotation)
    camera_z_change = find_polar_z_change(x_rotation)


# cartesian
def find_cartesian_change(point):
    return point-camera_x


# return the vector
def cartesian_vector(x, y, z):
    global point_x_change
    global point_y_change
    global point_z_change
    point_x_change = find_cartesian_change(x)
    point_y_change = find_cartesian_change(y)
    point_z_change = find_cartesian_change(z)


# find the angle between the two vectors
def find_z_angle():
    dot_product = \
        camera_x_change * point_x_change + camera_y_change * point_y_change
    magnitude_product = \
        math.sqrt(camera_x_change ** 2 + camera_y_change ** 2) * \
        math.sqrt(point_x_change ** 2 + point_y_change ** 2)
    global z_angle
    z_angle = \
        round(math.degrees(math.acos((dot_product)/(magnitude_product))), ndigits=4)
    # this make it sign sensitive so that it can tell if the angle is positive or negative
    z_angle *= ((camera_x_change * 1.2 + 1) / abs((camera_x_change * 1.2 + 1))
                ) * ((point_x_change * 1.2 + 1) / abs((point_x_change * 1.2 + 1)))


def find_x_angle():
    dot_product = \
        camera_z_change * point_z_change + camera_y_change * point_y_change
    magnitude_product = \
        math.sqrt(camera_z_change ** 2 + camera_y_change ** 2) * \
        math.sqrt(point_z_change ** 2 + point_y_change ** 2)
    global x_angle
    x_angle = \
        round(math.degrees(math.acos((dot_product) / (magnitude_product))), ndigits=4)
    # this make it sign sensitive so that it can tell if the angle is positive or negative
    x_angle *= ((camera_z_change * 1.2 + 1) / abs((camera_z_change * 1.2 + 1))
                ) * (point_z_change * 1.2 + 1) / abs((point_z_change * 1.2 + 1))


def find_angle():
    find_z_angle()
    find_x_angle()


# given the x and y angle, find the x and y coordinate for each coresponding point

def find_x_coordinate():
    global x_coordinate
    x_coordinate = \
        round(math.tan(math.radians(z_angle)),
              ndigits=4) * camera_x_y_magnitude


def find_y_coordinate():
    global y_coordinate
    y_coordinate = \
        round(math.tan(math.radians(x_angle)),
              ndigits=4) * camera_y_z_magnitude


def find_coordinate():
    find_x_coordinate()
    find_y_coordinate()


# camera polar definition
z_rotation = 62
x_rotation = 53

camera_display_length = 2
# looking only at the x and y axsis, what is the magnitude
camera_x_y_magnitude = camera_display_length * \
    round(math.cos(math.radians(x_rotation)), ndigits=4)
# looking only at the y and z axsis, what is the magnitude
camera_y_z_magnitude = camera_display_length * \
    round(math.cos(math.radians(z_rotation)), ndigits=4)

# these are equivilient to x_orgin, y_orgin, z_orgin
camera_x = 0
camera_y = 0
camera_z = 0

# camera vector
camera_x_change = 1
camera_y_change = 1
camera_z_change = 1

# point vector
point_x_change = 1
point_y_change = 1
point_z_change = 1

# angles between the two vectors
z_angle = 1
x_angle = 1

# point coordinates
x_coordinate = 1
y_coordinate = 1

camera = polar_vector()
point = cartesian_vector(2, 4, 2)
angles = find_angle()
coordinate = find_coordinate()
print(camera_x_change, camera_y_change, camera_z_change)
print(point_x_change, point_y_change, point_z_change)
print(z_angle, x_angle)
print(x_coordinate, y_coordinate)
