from random import randint
from random import random
from player import Player
from field import Field
from my_errors import CollisionError

class Enemy(Player):
    def __init__(self):
        super().__init__()
        self.shots = []

    def set_ships(self):
        """Подготовленные поля противника"""
        list_fields = [[['■', '■', '■', 'О', 'О', 'О'], ['О', 'О', 'О', 'О', '■', 'О'], ['■', 'О', '■', 'О', '■', 'О'],
                        ['О', 'О', 'О', 'О', 'О', 'О'], ['О', 'О', 'О', '■', 'О', '■'], ['■', '■', 'О', 'О', 'О', 'О']],
                       [['■', '■', 'О', 'О', '■', 'О'], ['О', 'О', 'О', 'О', 'О', 'О'], ['О', '■', 'О', '■', 'О', 'О'],
                        ['■', 'О', 'О', 'О', 'О', '■'], ['■', 'О', '■', 'О', 'О', '■'], ['О', 'О', 'О', 'О', 'О', '■']],
                       [['■', 'О', '■', '■', 'О', '■'], ['■', 'О', 'О', 'О', 'О', 'О'], ['■', 'О', 'О', 'О', '■', 'О'],
                        ['О', 'О', '■', 'О', 'О', 'О'], ['О', 'О', '■', 'О', '■', 'О'], ['■', 'О', 'О', 'О', 'О', 'О']],
                       [['О', 'О', 'О', '■', 'О', '■'], ['О', '■', 'О', 'О', 'О', 'О'], ['О', '■', 'О', '■', 'О', '■'],
                        ['О', 'О', 'О', 'О', 'О', '■'], ['О', 'О', 'О', 'О', 'О', '■'], ['■', 'О', '■', '■', 'О', 'О']]
                       ]
        # self.field.set_field(list_fields[0])

        for ship in self.Ships:
            while True:
                pos = (randint(0, 5), randint(0, 5))
                if ship.get_size > 1:
                    ship.orientation = True if random() == 1 else False
                try:
                    ship.position = pos
                except CollisionError:
                    continue
                except IndexError:
                    continue
                break
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
