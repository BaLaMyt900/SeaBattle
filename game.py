from user import User
from enemy import Enemy


class Game:
    def __init__(self):
        self.user = User()
        self.enemy = Enemy()
        self.game = True

    def __greet(self):
        print('Добро подаловать в Игру "Морской бой"!')
        print("Для начала необходимо выставить корабли.")
        print('Если Вы поставили корабли неправильно, введите retry для обнуления поля.')
        self.user.set_ships()
        self.enemy.set_ships()
        print("Перед Вами два поля. Слева Ваше. Справа противника.")
        print("Для выстрела, введите координаты стрельбы Y X через пробел")

    def __user_turn(self):
        while self.user.shot(self.enemy.field):
            print('Попадание! Стреляйте еще раз!')
            area = self.enemy.check_down_ship()
            if area:
                for y, x in area:
                    self.user.field_for_shot.field[y][x] = 'T'
                print('Корабль противника Потоплен! Так держать!')
            if self.enemy.check_defeat():
                print('Все корабли противника потоплены. Поздравляю с победой!')
                self.game = False
                break
        print('Промах!')

    def __enemy_turn(self):
        while self.enemy.shot(self.user.field):
            print('В Ваш корабль попали!')
            if self.user.check_down_ship():
                print('Ваш корабль затонул!')
            if self.user.check_defeat():
                print('Все ваши корабли потоплены. Поражение!')
                self.game = False
                break
        print('Противник промахнулся!')

    def __loop(self):
        while self.game:
            self.__user_turn()
            if not self.game:  # Небольшой костыль. Для завершения игры, после победы игрока
                break
            self.__enemy_turn()

    def start(self):
        self.__greet()
        self.__loop()
