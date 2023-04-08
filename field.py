from my_errors import CollisionError

class Field:
    def __init__(self):
        self.field = [['О' for i in range(6)] for d in range(6)]


    def field(self):
        return self.field

    def set_field(self, var: list):
        self.field = var

    """Принимает лист с кортежами и пытается записать в поле. Иначе ошибка"""
    def set_ship(self, dot: list):
        for d in dot:
            """Проверка нахождения в пределах индексов"""
            if not 0 <= d[0] <= 5 or not 0 <= d[1] <= 5:
                raise IndexError
            """Поле 3х3 вокруг точки"""
            check = [(x, y) for x in range(d[0]-1, d[0]+2) for y in range(d[1]-1, d[1]+2)]
            for ch in check:
                """Оборачиваем в try ибо может быть за пределами поля"""
                try:
                    if d[0] > 0 and d[1] > 0:
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
