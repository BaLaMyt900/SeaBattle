from random import randint
from player import Player
from field import Field
from my_errors import CollisionError


class Enemy(Player):
    def __init__(self):
        super().__init__()
        self.shots = []

    def set_ships(self):  # Генератор поля компьютера.
        while True:
            tries = 0
            self.field.field = [['О' for _ in range(6)] for _ in range(6)]
            for ship in self.Ships:
                while tries < 100:
                    if ship.size > 1:
                        ship.orientation = True if randint(0, 1) == 1 else False
                    try:
                        ship.position = (randint(0, 5), randint(0, 5))
                    except CollisionError:
                        tries += 1
                        continue
                    except IndexError:
                        tries += 1
                        continue
                    else:
                        break
            check = all([True if ship.position else False for ship in self.Ships])
            if self.field.field != [['О' for _ in range(6)] for _ in range(6)] and check:
                break

    def shot(self, enemy_field: Field):  # Функция выстрела компьютера
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
