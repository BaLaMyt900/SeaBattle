from my_errors import CollisionError

class Field:
    def __init__(self):
        self.field = [['О' for i in range(6)] for d in range(6)]

    def set_field(self, var: list):
        self.field = var


    """Принимает лист с кортежами и пытается записать в поле. Иначе ошибка"""
    def set_ship(self, dots: list):
        for y, x in dots:
            if not 0 <= y <= 5 and not 0 <= x <= 5:
                raise IndexError
            check = [(y_, x_) for x_ in range(x - 1, x + 2) for y_ in range(y - 1, y + 2)]
            for y_, x_ in check:
                if 5 >= y_ >= 0 and 5 >= x_ >= 0:
                    if self.field[y_][x_] == '■':
                        raise CollisionError
        for y, x in dots:
            self.field[y][x] = '■'


    """Отрисовка поля"""
    def draw_field(self):
        print(f"  {' '.join(f'| {i} |' for i in range(6))}")
        for i, st in enumerate(self.field):
            print(f'{i} {" ".join(f"| {s} |" for s in st)}')

    """Проверка попадания"""
    def check_hit(self, shot: tuple):
        if self.field[shot[0]][shot[1]] == '■':
            self.field[shot[0]][shot[1]] = 'X'
            return True
        else:
            self.field[shot[0]][shot[1]] = 'T'
            return False
