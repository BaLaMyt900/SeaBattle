from random import randint, random
from progress.bar import FillingCirclesBar

class CollisionError(Exception):
    def __init__(self):
        pass

class Field:
    def __init__(self):
        self.field = [['О' for i in range(6)] for d in range(6)]

    """Отрисовка поля"""
    def get_field(self):
        return self.field

    """Принимает лист с кортежами и пытается записать в поле. Иначе ошибка"""
    def set_shit(self, dot: list):
        for d in dot:
            """Поле 3х3 вокруг точки"""
            check = [(x, y) for x in range(d[0]-1, d[0]+2) for y in range(d[1]-1, d[1]+2)]
            for ch in check:
                """Оборачиваем в try ибо может быть за пределами поля"""
                try:
                    if self.field[ch[0]][ch[1]] != 'О':
                        raise CollisionError
                except CollisionError:
                    raise CollisionError
                except IndexError:
                    pass
        for d in dot:
            try:
                self.field[d[0]][d[1]] = '■'
            except IndexError:
                raise IndexError

    def draw_field(self):
        print(f"  {' '.join(f'| {i} |' for i in range(6))}")
        for i, st in enumerate(self.field):
            print(f'{i} {" ".join(f"| {s} |" for s in st)}')


class Ship:
    _position = (0, 0)
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
                self.field.set_shit(position)
            except CollisionError:
                raise CollisionError
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




class Player:
    def __init__(self):
        self.field = Field()
        self.enemy_field = Field()
        self.Ships = [Ship(3, self.field), Ship(2, self.field),
                      Ship(2, self.field), Ship(1, self.field),
                      Ship(1, self.field), Ship(1, self.field),
                      Ship(1, self.field)]

    def set_ships(self):
        for ship in self.Ships:
            while True:
                self.field.draw_field()
                pos = input(f'Введите координаты для {f"{ship.get_size}х" if ship.get_size > 1 else f"{ship.get_size}но"} палубного корабля. Y X через пробел: ')
                try:
                    pos = (int(pos[0]), int(pos[2]))
                except:
                    print('Неверный ввод. Повторите снова')
                    continue
                if not 0 <= pos[0] <= 5 or not 0 <= pos[1] <= 5:
                    print('Выход за координаты. Повторите попытку')
                    continue
                if ship.get_size > 1:
                    orientation = input('Установить вертикально? Введите Y')
                    ship.orientation = True if any([orientation == 'Y', orientation == 'y',
                                                    orientation == 'н', orientation == 'Н']) else False
                try:
                    ship.position = pos
                except CollisionError:
                    print('Ошибка. Недопустимые координаты.')
                    continue
                break

    def set_enemy_ships(self):
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

def init():
    # player = Player()
    # player.set_ships()
    Enemy = Player()
    print('Генерация поля противника...')
    Enemy.set_enemy_ships()

def main():
    init()


if __name__ == '__main__':
    main()
