# https://www.geogebra.org/calculator/ghwysc7z Geogebra representation
# I know the documentations are horrible, working on it...
# This code right know
# Gavin 2022

import math


class Point:
    def __init__(self, x_orgin, y_orgin, z_orgin):
        self.x_orgin = x_orgin
        self.y_orgin = y_orgin
        self.z_orgin = z_orgin

    # polar
    def find_polar_x_change(self, z_rotation, up_down_rotation, radius):
        return round(math.sin(math.radians(z_rotation)), ndigits=4) * camera_x_y_magnitude

    def find_polar_y_change(self, z_rotation, up_down_rotation, radius):
        return round(math.cos(math.radians(z_rotation)), ndigits=4) * camera_x_y_magnitude

    def find_polar_z_change(self, z_rotation, up_down_rotation, radius):
        return round(math.sin(math.radians(up_down_rotation)), ndigits=4) * camera_y_z_magnitude

    # return the vector

    def polar_vector(self, z_rotation, x_rotation, radius):
        return [self.find_polar_x_change(z_rotation, x_rotation, radius), self.find_polar_y_change(z_rotation, x_rotation, radius), self.find_polar_z_change(z_rotation, x_rotation, radius)]

    # cartesian

    def find_cartesian_x_change(self, x, y, z):
        return x-self.x_orgin  # - x  # if self.x_orgin > x else x - self.x_orgin

    def find_cartesian_y_change(self, x, y, z):
        return y-self.y_orgin  # - y  # if self.y_orgin > y else y - self.y_orgin

    def find_cartesian_z_change(self, x, y, z):
        return z-self.z_orgin  # - z  # if self.z_orgin > z else z - self.z_orgin
    # return the vector

    def cartesian_vector(self, x, y, z):
        return [self.find_cartesian_x_change(x, y, z), self.find_cartesian_y_change(x, y, z), self.find_cartesian_z_change(x, y, z)]


def find_angle_between(vector1, vector2):
    def find_z_angle():
        dot_product = vector1[0] * vector2[0] + vector1[1] * vector2[1]
        magnitude_product = math.sqrt(
            vector1[0] ** 2 + vector1[1] ** 2) * math.sqrt(vector2[0] ** 2 + vector2[1] ** 2)
        z_angle = round(math.degrees(
            math.acos((dot_product)/(magnitude_product))), ndigits=4)
        return z_angle * ((vector1[0] * 1.2 + 1) / abs((vector1[0] * 1.2 + 1))) * ((vector2[0] * 1.2 + 1) / abs((vector2[0] * 1.2 + 1)))

    def find_x_angle():
        dot_product = vector1[2] * vector2[2] + vector1[1] * vector2[1]
        magnitude_product = math.sqrt(
            vector1[2] ** 2 + vector1[1] ** 2) * math.sqrt(vector2[2] ** 2 + vector2[1] ** 2)
        x_angle = round(math.degrees(
            math.acos((dot_product) / (magnitude_product))), ndigits=4)
        return x_angle * ((vector1[2] * 1.2 + 1) / abs((vector1[2] * 1.2 + 1))) * (vector2[2] * 1.2 + 1) / abs((vector2[2] * 1.2 + 1))
    return [find_z_angle(), find_x_angle()]

# given the x and y angle, find the x and y coordinate for each coresponding point


def find_coordinate_for(degree, camera_display_length, z_rotation, up_down_rotation):
    def find_x_coordinate():
        return round(math.tan(math.radians(degree[0])), ndigits=4) * camera_x_y_magnitude

    def find_y_coordinate():
        return round(math.tan(math.radians(degree[1])), ndigits=4) * camera_y_z_magnitude
    return [find_x_coordinate(), find_y_coordinate()]


z_rotation = 62
up_down_rotation = 53
camera_display_length = 2

# looking only at the x and y axsis, what is the magnitude
camera_x_y_magnitude = camera_display_length * \
    round(math.cos(math.radians(up_down_rotation)), ndigits=4)
# looking only at the y and z axsis, what is the magnitude
camera_y_z_magnitude = camera_display_length * \
    round(math.cos(math.radians(z_rotation)), ndigits=4)


def main():
    camera = Point(0, 0, 0).polar_vector(
        z_rotation, up_down_rotation, camera_display_length)
    point = Point(0, 0, 0).cartesian_vector(2, 4, 2)
    print(camera)
    print(point)
    angles = find_angle_between(camera, point)
    coordinate = find_coordinate_for(
        angles, camera_display_length, z_rotation, up_down_rotation)
    print(angles)
    print(coordinate)


main()
