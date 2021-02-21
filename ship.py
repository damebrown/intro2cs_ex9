from random import randint

MAX_TORPEDO_AMOUNT = 15

class Ship():
    """
    this class is represents the ship in the game. it defines the ship's
    attributes which are five- location on x axis, location on y axis,
    velocity on y axis, velocity on x axis and the ship's direction.
    """

    def __init__(self, x_loc=randint(-500,500), y_loc=randint(-500,500), x_velocity=0, y_velocity=0, orientation=0):
        """
        this function defines the attributes for the ship class which are:
        :param x_loc: location on x axis
        :param y_loc: location on y axis
        :param x_velocity: velocity on x axis
        :param y_velocity: velocity on y axis
        :param orientation: the ship's direction
        """
        self.__x_location = x_loc
        self.__y_location = y_loc
        self.__x_velocity = x_velocity
        self.__y_velocity = y_velocity
        self.__orientation = orientation
        self.__life = 3

    def get_x_loc(self):
        """
        :return: location of the instance of class ship on x axis
        """
        return self.__x_location

    def get_y_loc(self):
        """
        :return: location of the instance of class ship on y axis
        """
        return self.__y_location
    def set_y_loc(self,location):
        self.__y_location = location

    def set_x_loc(self,location):
        self.__x_location = location

    def get_life(self):
        """this function returns the amount of life left to the ship"""
        return self.__life

    def got_hit(self):
        """this function reduces one life point from the ship"""
        if self.__life == 1:
            return False
        else:
            self.__life -= 1
            return True


    def get_x_vel(self):
        """
        :return: speed of the instance of class ship on x axis
        """
        return self.__x_velocity

    def get_y_vel(self):
        """
        :return: speed of the instance of class ship on y axis
        """
        return self.__y_velocity

    def get_radius(self):
        """This function returns the radius of the ship"""
        radius = 1
        return radius

    def get_orientation(self):
        """
        :return: return's ship's orientation
        """
        return self.__orientation

    def set_ship_orientation(self, degree):
        self.__orientation += degree
        if self.__orientation >=360 or self.__orientation <= -360:
            self.__orientation = 0

    def ship_accelerate_x(self, speed):
        if self.__x_velocity < 10 and self.__x_velocity > -10:
            self.__x_velocity = speed

    def ship_accelerate_y(self, speed):
        if self.__y_velocity < 10 and self.__y_velocity > -10:
            self.__y_velocity = speed


