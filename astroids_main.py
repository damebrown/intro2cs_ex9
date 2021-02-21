from screen import Screen
import sys
from ship import Ship
import math
from astroid import Astroid
import random

DEFAULT_ASTEROIDS_NUM = 5
ROTATE_UP = 7
ROTATE_DOWN = -7
class GameRunner:

    def __init__(self, asteroids_amnt=5):
        self._screen = Screen()
        self.__asteroids_amnt = asteroids_amnt
        self.screen_max_x = Screen.SCREEN_MAX_X
        self.screen_max_y = Screen.SCREEN_MAX_Y
        self.screen_min_x = Screen.SCREEN_MIN_X
        self.screen_min_y = Screen.SCREEN_MIN_Y
        self.__ship = Ship()
        self.__asteroids_list = []

    def place_astroids(self):
        """this function places asteroids on the screen"""
        for asteroid in range(self.__asteroids_amnt):
            curr_loc_x = random.randint(-500,500)
            curr_loc_y = random.randint(-500,500)
            while curr_loc_x == self.__ship.get_x_loc() and curr_loc_y == \
                    self.__ship.get_y_loc():
                curr_loc_x = random.randint(-500, 500)
                curr_loc_y = random.randint(-500, 500)
            curr_asteroid = Astroid(curr_loc_x,random.randint(0,10)-5,
                    curr_loc_y,random.randint(0,10)-5)

            self.__asteroids_list.append(curr_asteroid)
            self._screen.register_asteroid(curr_asteroid,
                             curr_asteroid.get_size())


    def run(self):
        self._do_loop()
        self._screen.start_screen()

    def _do_loop(self):
        # You don't need to change this method!
        self._game_loop()

        # Set the timer to go off again
        self._screen.update()
        self._screen.ontimer(self._do_loop,5)

    def draw_asteroids(self):
        for asteroid in self.__asteroids_list:
            self._screen.draw_asteroid(asteroid,asteroid.get_x_loc,
                                       asteroid.get_y_loc)

    def move_asteroids(self):
        for asteroid in self.__asteroids_list:
            self.x_movement(asteroid)
            self.y_movement(asteroid)


    def x_movement(self, obj):
        """
        calculates the movement of ship on x axis according to the given
        formula
        :param ship: the item wanted moved
        :return: ship's new x coordinates according to it's speed and location
        """
        new_coord_x = (obj.get_x_vel() + obj.get_x_loc() - self.screen_min_x)\
                % (self.screen_max_x - self.screen_min_x) + self.screen_min_x
        obj.set_x_loc(new_coord_x)

    def y_movement(self, obj):
        """
        calculates the movement of ship on y axis according to the given
        formula
        :param ship: the item wanted moved
        :return: ship's new y coordinates according to it's speed and location
        """
        new_coord_y = (obj.get_y_vel() + obj.get_y_loc() - self.screen_min_y) \
                % (self.screen_max_y - self.screen_min_y) + self.screen_min_y
        obj.set_y_loc(new_coord_y)

    def rotation(self):
        """this function deals with the rotation of the ship"""
        if self._screen.is_left_pressed():
            self.__ship.set_ship_orientation(ROTATE_UP)
        if self._screen.is_right_pressed():
            self.__ship.set_ship_orientation(ROTATE_DOWN)

    def all_movments(self):
        self.all_movments_for_the_ship()
        self.move_asteroids()

    def all_movments_for_the_ship(self):
        """this function deals with all the movments of the ship"""
        self.rotation()
        self.accelerate()
        self.x_movement(self.__ship)
        self.y_movement(self.__ship)

    def accelerate(self):
        """this function is in charge of accelerating the ship"""
        if self._screen.is_up_pressed():
            self.accelerate_ship_x(),\
            self.accelerate_ship_y()

    def accelerate_ship_x(self):
        """this function is accelerating the ship on the x axis"""
        new_speed = self.__ship.get_x_vel() + math.cos(math.radians(
            self.__ship.get_orientation()))
        self.__ship.ship_accelerate_x(new_speed)

    def accelerate_ship_y(self):
        """this function is accelerating the ship on the x axis"""
        new_speed = self.__ship.get_y_vel() + math.sin(math.radians(
            self.__ship.get_orientation()))
        self.__ship.ship_accelerate_y(new_speed)

    def collision(self):
        for asteroid in self.__asteroids_list:
            if asteroid.has_intesection(self.__ship):
                if self.__ship.got_hit():
                    #then we stop the game because he's dead!
                    pass
                else:
                    self._screen.show_message("You hit an asteroid!",
                        "remaining life is :"+str(self.__ship.get_life()))
                    self._screen.unregister_asteroid(asteroid)

    def draw_all(self):
        self._screen.draw_ship(self.__ship.get_x_loc(), self.__ship.get_y_loc()
                               , self.__ship.get_orientation())
        self.draw_asteroids()

    def _game_loop(self):
        self.collision()
        self.all_movments()
        self.draw_all()

        print("speed x :"+str(self.__ship.get_x_vel()),"speed y : " + str(
            self.__ship.get_y_vel()),"loc x : "+str(self.__ship.get_x_loc()),
              "loc y: "+str(self.__ship.get_y_loc()),"angle is "+ str(
                self.__ship.get_orientation()))

def main(amnt):
    runner = GameRunner(amnt)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main( int( sys.argv[1] ) )
    else:
        main( DEFAULT_ASTEROIDS_NUM )