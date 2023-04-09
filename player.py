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

    def set_ships(self):  # Установка кораблей с проверкой ввода и обработка ошибок
        for ship in self.Ships:
            while True:
                self.field.draw_field()
                pos = input(f'Введите координаты для {f"{ship.size}х" if ship.size > 1 else f"{ship.size}но"}'
                            f' палубного корабля. Y X через пробел: ')
                try:
                    pos = (int(pos[0]), int(pos[2]))
                except ValueError:
                    print('Неверный ввод. Повторите снова')
                    continue
                if not 0 <= pos[0] <= 5 or not 0 <= pos[1] <= 5:
                    print('Выход за координаты. Повторите попытку')
                    continue
                if ship.size > 1:
                    orientation = input('Установить вертикально? Введите Y')
                    ship.orientation = True if any([orientation == 'Y', orientation == 'y',
                                                    orientation == 'н', orientation == 'Н']) else False
                try:
                    ship.position = pos
                except CollisionError:
                    print('Ошибка. Слишком близко к другому кораблю.')
                    continue
                except IndexError:
                    print('Ошибка. Корабль установлен за пределами карты.')
                    continue
                break

    def draw_both_field(self):  # Отрисовка своего поля и поля для стрельбы через табуляцию
        print(f"  {' '.join(f'| {i} |' for i in range(6))}\t  {' '.join(f'| {i} |' for i in range(6))}")
        for i, st in enumerate(zip(self.field.field, self.field_for_shot.field)):
            print(f'{i} {" ".join(f"| {s} |" for s in st[0])}\t{i} {" ".join(f"| {s} |" for s in st[1])}')

    def shot(self, enemy_field: Field):  # Функция стрельбы пользователя.
        while True:
            shot = input('Введите координаты: ')
            try:
                shot = (int(shot[0]), int(shot[2]))
            except ValueError:
                print('Неверный ввод. Необходимо ввести Y X от 0 до 5 через пробел.')
                continue
            if not 0 <= shot[0] <= 5 or not 0 <= shot[1] <= 5:
                print('Выход за границу карты. Необходимо ввести значение от 0 до 5.')
                continue
            if self.field_for_shot.field[shot[0]][shot[1]] == 'T' or self.field_for_shot.field[shot[0]][shot[1]] == 'X':
                print('Вы уже туда стреляли. Введите другие координаты.')
                continue
            else:
                if enemy_field.check_hit(shot):
                    self.field_for_shot.field[shot[0]][shot[1]] = 'X'
                    return True
                else:
                    self.field_for_shot.field[shot[0]][shot[1]] = 'T'
                    return False

    def check_down_ship(self):  # Проверка потопленных кораблей. Возвращает Истину если нашелся хоть один и удаляет его
        for ship in self.Ships:
            if ship.check_down():
                self.Ships.remove(ship)
                return True
        return False

    def check_defeat(self):  # Проверка поражения. Если список кораблей пуст, возвращает Истину
        return len(self.Ships) == 0
