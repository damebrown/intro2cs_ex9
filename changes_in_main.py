ACCELERATION_FACTOR = 2

def set_torpedo_x_vel(self):
	"""
	this function calculates the speed of a torpedo on the x axis
	using the given formula.
	:return: the torpedo's speed on the x axis
	"""
	rad_direct = math.radians(self.__ship.get_orientation())
	x_speed = self.__ship.get_x_vel() + ACCELERATION_FACTOR * math.cos \(rad_direct)
	return x_speed

def set_torpedo_y_vel(self):
	"""
	this function calculates the speed of a torpedo on the y axis
	using the given formula.
	:return: the torpedo's speed on the y axis
	"""
	rad_direction = math.radians(self.__ship.get_orientation())
	y_speed = self.__ship.get_y_vel() + ACCELERATION_FACTOR * math.sin \
		(rad_direction)
	return y_speed

def torpedo_management(self):
	"""
	this function manages the creation, deletion, drawing and defining
	all the games torpedoes.
	"""
	self.lives_manager(  )  # checkes if the life span of the torpedo is over
	if self._screen.is_space_pressed() and self.torpedo_counter():
		# creation of a new torpedo in case of space being pressed
		cur_torpedo = Torpedo(self.set_torpedo_x_vel(),
		                      self.set_torpedo_y_vel(),
		                      self.__ship.get_x_loc(),
		                      self.__ship.get_y_loc(),
		                      self.__ship.get_orientation())
		# registering torpedo
		self._screen.register_torpedo(cur_torpedo)
		# appending torpedo to torpedoes list
		self.__torpedoes_list.append(cur_torpedo)
		# drawing torpedo
		self._screen.draw_torpedo(cur_torpedo, cur_torpedo.get_x_loc(),
		                          cur_torpedo.get_y_loc(),
		                          cur_torpedo.get_orientation())

def lives_manager(self):
	"""
	this function manages the life span of each torpedo, and making sure
	that there is no torpedo that is older the 200 iterations old
	"""
	for index, torpedo in enumerate(self.__torpedoes_list):
		torpedo.set_lives_counter()  # updating torpedo's live's count
		if torpedo.get_lives_counter() >= MAX_TORPEDO_AGE:
			# making sure that no old torpedo survives
			self._screen.unregister_torpedo(torpedo)
			self.__torpedoes_list.pop(index)

def torpedo_counter(self):
	"""
	this function helps enforce that there are no more than 15
	torpedoes in the game.
	"""
	if len(self.__torpedoes_list) < MAX_TORPEDO_AMOUNT:
		return True
	else:
		return False

def draw_all_torpedos(self):
	"""
	this function is managing all drawing of all torpedoes
	"""
	for torpedo in self.__torpedoes_list:
		# updating the torpedo's location according to the given formula
		self.x_movement(torpedo), self.y_movement(torpedo)
		# drawing each and every torpedo in torpedoes list
		self._screen.draw_torpedo(torpedo, torpedo.get_x_loc(),
		                          torpedo.get_y_loc(),
		                          torpedo.get_orientatn())

def game_ending_manager(self):
	"""
	this function manages every case in which the game should end,
	and printing an informative question about the reason the game has
	ended.
	"""
	if self._screen.should_end():
		# if 'q' was pressed
		print('button q was pressed, and thus game ended')
		self._screen.end_game()
	elif self.__ship.get_life() == 0:
		# if ship has died
		print('you died, game is done')
		self._screen.end_game()
	elif self.__asteroids_list == []:
		# if asteroids are all dead
		print('you won! congrats!')
		self._screen.end_game()