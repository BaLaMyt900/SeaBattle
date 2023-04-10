from random import randint
from player import Player
from field import Field
from my_errors import CollisionError

class Enemy(Player):  # Пермутация от Player с перепесью функций
    def __init__(self):
        super().__init__()
        self.shots = []

    def set_ships(self):  # Выбор 1го из 4ех подготовленных полей
        while True:
            tries = 0
            self.field = Field().field
            for i, ship in enumerate(self.Ships):
                while tries < 1000:
                    print(tries)
                    try:
                        pos = (randint(0, 5), randint(0,5))
                        ship.position, ship.orientation = pos, True if randint(0, 1) == 1 else False
                        # ship.position = pos
                    except CollisionError:
                        print(i)
                        continue
                    except IndexError:
                        print(i)
                        continue
                    else:
                        break




    def shot(self, enemy_field: Field):  # Перепись функции выстрела.
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
