from random import randint
from player import Player
from field import Field


class Enemy(Player):  # Пермутация от Player с перепесью функций
    def __init__(self):
        super().__init__()
        self.shots = []

    def set_ships(self):  # Выбор 1го из 4ех подготовленных полей
        choise = 2
        if choise == 0:
            self.Ships[0].orientation, self.Ships[0].position = True, (4, 0)
            self.Ships[1].orientation, self.Ships[1].position = False, (0, 4)
            self.Ships[2].orientation, self.Ships[2].position = False, (5, 3)
            self.Ships[3].position = (0, 0)
            self.Ships[4].position = (2, 2)
            self.Ships[5].position = (2, 5)
            self.Ships[6].position = (5, 5)
        elif choise == 1:
            self.Ships[0].orientation, self.Ships[0].position = False, (0, 2)
            self.Ships[1].orientation, self.Ships[1].position = True, (3, 0)
            self.Ships[2].orientation, self.Ships[2].position = True, (1, 5)
            self.Ships[3].position = (2, 2)
            self.Ships[4].position = (5, 1)
            self.Ships[5].position = (4, 3)
            self.Ships[6].position = (4, 5)
        elif choise == 2:
            self.Ships[0].orientation, self.Ships[0].position = True, (2, 5)
            self.Ships[1].orientation, self.Ships[1].position = True, (2, 0)
            self.Ships[2].orientation, self.Ships[2].position = False, (5, 1)
            self.Ships[3].position = (0, 2)
            self.Ships[4].position = (2, 2)
            self.Ships[5].position = (4, 3)
            self.Ships[6].position = (5, 5)
        elif choise == 3:
            self.Ships[0].orientation, self.Ships[0].position = True, (2, 5)
            self.Ships[1].orientation, self.Ships[1].position = False, (0, 2)
            self.Ships[2].orientation, self.Ships[2].position = False, (5, 1)
            self.Ships[3].position = (2, 0)
            self.Ships[4].position = (2, 2)
            self.Ships[5].position = (5, 3)
            self.Ships[6].position = (5, 5)
        pass

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
