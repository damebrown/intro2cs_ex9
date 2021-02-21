from screen import Screen
import sys
from ship import Ship
import math

DEFAULT_ASTEROIDS_NUM = 5


class GameRunner:

    def __init__(self, asteroids_amnt):
        self._screen = Screen()

        self.screen_max_x = Screen.SCREEN_MAX_X
        self.screen_max_y = Screen.SCREEN_MAX_Y
        self.screen_min_x = Screen.SCREEN_MIN_X
        self.screen_min_y = Screen.SCREEN_MIN_Y

    def run(self):
        self._do_loop()
        self._screen.start_screen()

    def _do_loop(self):
        # You don't need to change this method!
        self._game_loop()

        # Set the timer to go off again
        self._screen.update()
        self._screen.ontimer(self._do_loop,5)

    def x_movement(self, ship):
        """
        calculates the movement of ship on x axis according to the given
        formula
        :param ship: the item wanted moved
        :return: ship's new x coordinates according to it's speed and location
        """
        new_coord = (ship.get_x_vel() + ship.get_x_loc() - self.screen_min_x)\
                    % (self.screen_max_x - self.screen_min_x) + self.screen_min_x
        return new_coord


    def y_movement(self, ship):
        """
        calculates the movement of ship on y axis according to the given
        formula
        :param ship: the item wanted moved
        :return: ship's new y coordinates according to it's speed and location
        """
        new_coord = (ship.get_y_vel() + ship.get_y_loc() - self.screen_min_y) \
                    % (self.screen_max_y - self.screen_min_y) + self.screen_min_y
        return new_coord


    def superposition(self, ship):
        setattr(ship, 'x_loc', x)
        setattr(ship, 'y_loc', y)


    def _game_loop(self):
        ship = Ship()
        if Screen.is_left_pressed(self):
            ship.set_ship_orientation(7)
        if Screen.is_right_pressed(self):
            ship.set_ship_orientation(-7)
        if Screen.is_up_pressed():
            self.accelerate_ship_x(ship), self.accelerate_ship_y(ship)
        x = self.x_movement(ship)
        y = self.y_movement(ship)
        Screen.draw_ship(x, y, ship.get_orientation())



    def accelerate_ship_x(self,ship):
        new_speed = ship.get_x_vel + math.cos(math.radians(ship.get_x_loc))
        ship.ship_accelerate_x(new_speed)

    def accelerate_ship_y(self, ship):
        new_speed = ship.get_y_vel + math.sin(math.radians(ship.get_y_loc))
        ship.ship_accelerate_y(new_speed)




def main(amnt):
    runner = GameRunner(amnt)
    runner.run()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main( int( sys.argv[1] ) )
    else:
        main( DEFAULT_ASTEROIDS_NUM )
