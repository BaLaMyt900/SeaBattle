from field import Field
from ship import Ship
from my_errors import CollisionError


class Player:
    def __init__(self):
        self.field = Field()
        self.field_for_shot = Field()
        self.Ships = [Ship(3, self.field), Ship(2, self.field),
                      Ship(2, self.field), Ship(1, self.field),
                      Ship(1, self.field), Ship(1, self.field),
                      Ship(1, self.field)]

    def check_down_ship(self):  # Проверка потопленных кораблей. Возвращает Истину если нашелся хоть один и удаляет его
        for ship in self.Ships:
            area = ship.check_down()
            if area:
                self.Ships.remove(ship)
                return area
        return False

    def check_defeat(self):  # Проверка поражения. Если список кораблей пуст, возвращает Истину
        return len(self.Ships) == 0
