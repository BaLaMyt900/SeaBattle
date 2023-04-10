from player import Player
from enemy import Enemy


class Game:
    def __init__(self):
        self.player = Player()
        self.enemy = Enemy()

    def __greet(self):
        print('Добро подаловать в Игру "Морской бой"!')
        print("Для начала необходимо выставить корабли.")
        print('Если Вы поставили корабли неправильно, введите retry для обнуления поля.')
        self.player.set_ships()
        self.enemy.set_ships()
        print("Перед Вами два поля. Слева Ваше. Справа противника.")
        print("Для выстрела, введите координаты стрельбы Y X через пробел")

    def __loop(self):
        while True:
            self.player.draw_both_field()
            while self.player.shot(self.enemy.field):
                print('Попадание! Стреляйте еще раз!')
                self.player.draw_both_field()
                if self.enemy.check_down_ship():
                    print('Корабль противника Потоплен! Так держать!')
                if self.enemy.check_defeat():
                    print('Все корабли противника потоплены. Поздравляю с победой!')
                    break
            print('Промах!')
            while self.enemy.shot(self.player.field):
                print('В Ваш корабль попали!')
                if self.player.check_down_ship():
                    print('Ваш корабль затонул!')
                if self.player.check_defeat():
                    print('Все ваши корабли потоплены. Поражение!')
                    break
            print('Противник промахнулся!')

    def start(self):
        self.__greet()
        self.__loop()
