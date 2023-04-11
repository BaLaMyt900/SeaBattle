from my_errors import CollisionError


class Field:
    def __init__(self):
        self.field = [['О' for _ in range(6)] for _ in range(6)]

    def set_ship(self, dots: list):  # Принимает лист с кортежами и пытается записать в поле. Иначе ошибка
        area = []
        for y, x in dots:
            if not 0 <= y <= 5 or not 0 <= x <= 5:
                raise IndexError
            check = [(y_, x_) for x_ in range(x - 1, x + 2) for y_ in range(y - 1, y + 2)]
            area.append(check)
            for y_, x_ in check:
                if 0 <= y_ <= 5 and 0 <= x_ <= 5:
                    try:
                        if self.field[y_][x_] == '■':
                            raise CollisionError
                    except CollisionError:
                        raise CollisionError
                    except IndexError:
                        pass
        for y, x in dots:
            self.field[y][x] = '■'
        return area  # Возврат окружения кораблю, для выстраивания логики затопления

    def check_hit(self, shot: tuple):  # Проверка попадания
        if self.field[shot[0]][shot[1]] == '■':
            self.field[shot[0]][shot[1]] = 'X'
            return True
        else:
            self.field[shot[0]][shot[1]] = 'T'
            return False
