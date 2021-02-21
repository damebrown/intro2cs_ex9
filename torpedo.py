import screen
import ship
import math

TORPEDO_RADIUS = 4
MAX_TORPEDO_AGE = 200


class Torpedo():
	"""
	this class's instances are torpedos shot by the ship at the asteroids
	"""

	def __init__(self, x_velocity, y_velocity, x_loc, y_loc, orientation,
	lives_counter = 0):
		self.__x_loc = x_loc
		self.__y_loc = y_loc
		self.__x_velocity = x_velocity
		self.__y_velocity = y_velocity
		self.__orientation = orientation
		self.__lives_counter = lives_counter

	def get_orientation(self):
		"""
		this function returns the orientation of the Torpedo's class instance
		"""
		return self.__orientation

	def get_x_loc(self):
		"""
		this function returns the location on X axis of the torpedo
		"""
		return self.__x_loc

	def get_y_loc(self):
		"""
		this function returns the location on Y axis of the torpedo
		"""
		return self.__y_loc

	def get_x_vel(self):
		"""
		this function returns the speed on X axis of the torpedo
		"""
		return self.__x_velocity

	def get_y_vel(self):
		"""
		this function returns the speed on Y axis of the torpedo
		"""
		return self.__y_velocity

	def set_x_loc(self, new_loc):
		"""
		this function gets a new location on x axis and updates the instance's
		location the on X axis
		:param new_loc: the new location, calculated using a given formula
		:return: updated location on X axis
		"""
		self.__x_loc = new_loc

	def set_y_loc(self, new_loc):
		"""
		this function gets a new location on Y axis and updates the
		instance's location the on Y axis
		:param new_loc: the new location, calculated using a given formula
		:return: updates the location on Y axis
		"""
		self.__y_loc = new_loc

	def get_lives_counter(self):
		"""
		this function returns the lives count of the torpedo
		:return: torpedo's life count
		"""
		return self.__lives_counter

	def set_lives_counter(self):
		"""
		this function changes the lives count of the class's instance
		"""
		self.__lives_counter += 1

	def get_radius(self):
		"""
		:return: returns the torpedoes radius, which is a global varient
		"""
		return TORPEDO_RADIUS




