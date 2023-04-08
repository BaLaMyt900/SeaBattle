from my_errors import CollisionError
from field import Field

class Ship:
    _position = [(0, 0)]
    _orientation = False

    def __init__(self, size: int, field: Field):
        self.size = size
        self.field = field

    @property
    def get_size(self):
        return self.size

    @property
    def orientation(self):
        return self._orientation

    @orientation.setter
    def orientation(self, orientation: bool):
        if self.size == 1:
            raise ValueError("Нет необходимости ставить ориентацию")
        else:
            self._orientation = orientation

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, pos: tuple):
        def set(position):
            try:
                self.field.set_ship(position)
            except CollisionError:
                raise CollisionError
            except IndexError:
                raise IndexError
            else:
                self._position = position

        if self.size == 3:
            if self._orientation:
                position = [(pos[0]-1, pos[1]), (pos[0], pos[1]), (pos[0]+1, pos[1])]
                set(position)
            else:
                position = [(pos[0], pos[1]-1), (pos[0], pos[1]), (pos[0], pos[1]+1)]
                set(position)
        elif self.size == 2:
            if self._orientation:
                position = [(pos[0]-1, pos[1]), (pos[0], pos[1])]
                set(position)
            else:
                position = [(pos[0], pos[1]-1), (pos[0], pos[1])]
                set(position)
        else:
            position = [(pos[0], pos[1])]
            set(position)

    def check_down(self):
        for pos in self._position:
            if self.field.field[pos[0]][pos[1]] == 'X':
                self.size -= 1
        return self.size == 0
