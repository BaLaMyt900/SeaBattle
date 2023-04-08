from random import randint
from player import Player
from field import Field
from my_errors import CollisionError


class Enemy(Player):
    def __init__(self):
        super().__init__()
        self.shots = []

    def set_ships(self):
        test_field = Field().field
        while True:
            self.field.field = test_field
            for ship in self.Ships:
                tries = 0
                while tries < 10:
                    pos = (randint(0, 5), randint(0, 5))
                    if ship.get_size > 1:
                        ship.orientation = True if randint(0, 1) == 1 else False
                    try:
                        ship.position = pos
                    except CollisionError:
                        tries += 1
                        continue
                    except IndexError:
                        tries += 1
                        continue
                    break

            if self.field.field != test_field:
                break
            else:
                self.field.draw_field()


    def shot(self, enemy_field: Field):
        while True:
            shot = (randint(0, 5), randint(0, 5))
            if shot not in self.shots:
                self.shots.append(shot)
                if enemy_field.check_hit(shot):
                    self.field_for_shot.field[shot[0]][shot[1]] = 'X'
                    return True
                else:
                    self.field_for_shot.field[shot[0]][shot[1]] = 'T'
                    return False
