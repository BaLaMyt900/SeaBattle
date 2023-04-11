from player import Player
from my_errors import CollisionError

class User(Player):
    def __init__(self):
        super().__init__()

    def set_ships(self):  # Установка кораблей с проверкой ввода и обработка ошибок
        for ship in self.Ships:
            if ship.position:
                break
            while True:
                self.draw_field()
                pos = input(f'Введите координаты для {f"{ship.size}х" if ship.size > 1 else f"{ship.size}но"}'
                            f' палубного корабля. Y X через пробел: ')
                if pos == 'retry':
                    self._wipe_field()
                    break
                try:
                    pos = (int(pos[0]), int(pos[2]))
                except ValueError:
                    print('Неверный ввод. Повторите снова')
                    continue
                except IndexError:
                    print('Введите значение')
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

    def _wipe_field(self):
        self.field.field = [['О' for _ in range(6)] for _ in range(6)]
        for ship in self.Ships:
            ship.wipe_position()
        self.set_ships()

    def draw_field(self):  # Отрисовка только своего поля
        print(f"  {' '.join(f'| {i} |' for i in range(6))}")
        for i, st in enumerate(self.field.field):
            print(f'{i} {" ".join(f"| {s} |" for s in st)}')

    def draw_both_field(self):  # Отрисовка своего поля и поля для стрельбы через табуляцию
        print(f"  {' '.join(f'| {i} |' for i in range(6))}\t  {' '.join(f'| {i} |' for i in range(6))}")
        for i, st in enumerate(zip(self.field.field, self.field_for_shot.field)):
            print(f'{i} {" ".join(f"| {s} |" for s in st[0])}\t{i} {" ".join(f"| {s} |" for s in st[1])}')

    def shot(self, enemy_field):  # Функция стрельбы пользователя.
        self.draw_both_field()
        while True:
            shot = input('Введите координаты: ')
            try:
                shot = (int(shot[0]), int(shot[2]))
            except ValueError:
                print('Неверный ввод. Необходимо ввести Y X от 0 до 5 через пробел.')
                continue
            except IndexError:
                print('Пустой ввод. Введите значения.')
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
