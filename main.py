class Field:
    def __init__(self):
        self.field = [['О' for i in range(6)] for d in range(6)]

    """Отрисовка поля"""
    def get_field(self):
        return self.field

    """Принимает кортеж с кортежами и пытается записать в поле. Иначе ошибка"""
    def set_shit(self, dot: tuple):
        """Проверка поля перед установкой корабля"""
        for d in dot:
            x, y = d[0]-1, d[1]-1
            for i in range(3):      # Проверяем X
                for e in range(3):  # Проверяем Y
                    try:   # Оборачиваем в try ибо может быть граница поля
                        if self.field[x][y] != 'O':
                            raise ValueError("Поле занято! Выберите другое место.")
                    except:
                        pass
                    finally:
                        y += 1
                x += 1
                y -= 3
        """Установка корабля"""
        for d in dot:
            self.field[d[0]][d[1]] = '■'

    def draw_field(self):
        print(f"  {' '.join(f'| {i} |' for i in range(1, 7))}")
        for i, st in enumerate(self.field):
            print(f'{i} {" ".join(f"| {s} |" for s in st)}')


class Ship:
    def __init__(self, size: int, field: Field):
        self.size = size
        self.field = field

    @property
    def position(self):
        return self.position

    @position.setter
    def position(self, pos: tuple):
        if self.size == 3:
            position = ((pos[0] - 1, pos[1]), (pos[0], pos[1]), (pos[0] + 1, pos[1]))
            try:
                self.field.set_shit(position)
            except ValueError:
                print('Позиция занята! Выберите другую!')
            else:
                self.position = position
        elif self.size == 2:
            position = ((pos[0] - 1, pos[1]), (pos[0], pos[1]))
            try:
                self.field.set_shit(position)
            except ValueError:
                print('Позиция занята! Выберите другую!')
            else:
                self.position = position
        else:
            position = ((pos[0], pos[1]))
            try:
                self.field.set_shit(position)
            except ValueError:
                print('Позиция занята! Выберите другую!')
            else:
                self.position = position

class Player:
    def __init__(self):
        self.field = Field()
        self.desk3_ship = Ship(3, self.field)
        self.desk2_ship1 = Ship(2, self.field)
        self.desk2_ship2 = Ship(2, self.field)
        self.desk1_ship1 = Ship(1, self.field)
        self.desk1_ship2 = Ship(1, self.field)
        self.desk1_ship3 = Ship(1, self.field)
        self.desk1_ship4 = Ship(1, self.field)

