import math
class Astroid:
    def __init__(self,x,x_speed,y,y_speed,size=3):
        """this class represents an astroid to be used by the game astroids
        it has 5 attributes, x and y location x speed, y speed, and the
        given size of the astroid as an integer from 1-3 """
        self.__x_loc = x
        self.__x_speed = x_speed
        self.__y_loc = y
        self.__y_speed = y_speed
        self.__size = size


    def get_size(self):
        """this function returns the size of the object"""
        return self.__size

    def get_x_vel(self):
        """this function returns the speed on the x line"""
        return self.__x_speed

    def get_y_vel(self):
        """this function returns the speed on the y line"""
        return self.__y_speed

    def get_x_loc(self):
        """this function returns the location x of the object"""
        return self.__x_loc

    def get_y_loc(self):
        """this function returns the location y of the object"""
        return self.__y_loc

    def set_x_loc(self, location):
        self.__x_loc = location

    def set_y_loc(self, location):
        self.__y_loc = location

    def get_radius(self):
        """This function returns the radius of the asteroid"""
        radius = (self.__size*10)-5
        return radius

    def has_intersection(self,obj):
        """this function checks if the have been collision"""
        distance = math.sqrt((obj.get_x_loc()-self.__x_loc)^2 +(
            obj.get_y_loc()-self.__y_loc)^2)
        if distance <= (self.get_radius()+obj.get_radius):
            return True
        else:
            return False

