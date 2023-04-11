from my_errors import CollisionError
from field import Field


class Ship:
    _position = []
    _orientation = False

    def __init__(self, size: int, field: Field):
        self.size = size
        self.field = field
        self.area = []

    @property
    def orientation(self):  # Ориентация. True Вертикально False Горизонтально
        return self._orientation

    @orientation.setter  # Установка ориентации
    def orientation(self, orientation: bool):
        if self.size == 1:
            self._orientation = False
        else:
            self._orientation = orientation

    @property
    def position(self):   # Позиция. Лист с координатами на поле
        return self._position

    @position.getter
    def position(self):
        return self._position

    @position.setter
    def position(self, pos: tuple):  # Установка позиции. Проверяет нахождение в поле, соседние клетки
        def set(position):
            try:
                areas = self.field.set_ship(position)
            except CollisionError:
                raise CollisionError
            except IndexError:
                raise IndexError
            else:
                self._position = position
                for area in areas:  # Пробегаемся по площадям, используя фильтры добавляем в площадь корабля
                    for dot in area:
                        if 0 <= dot[0] <= 5 and 0 <= dot[1] <= 5 and dot not in self._position:
                            self.area.append(dot)

        y, x = pos[0], pos[1]
        if self.size == 3:
            if self._orientation:
                set([(y-1, x), (y, x), (y+1, x)])
            else:
                set([(y, x-1), (y, x), (y, x+1)])
        elif self.size == 2:
            if self._orientation:
                set([(y-1, x), (y, x)])
            else:
                set([(y, x-1), (y, x)])
        else:
            set([(y, x)])

    def wipe_position(self):
        self._position = []

    def check_down(self):  # Проверка попаданий. Возвращает True если во все точки попали
        for dot in self._position:
            if self.field.field[dot[0]][dot[1]] == 'X':
                self.size -= 1
                self._position.remove(dot)
                if self.size == 0:
                    return self.area
        return False


