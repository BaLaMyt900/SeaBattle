from player import Player
from enemy import Enemy


class Game:
    def __init__(self):
        self.player = Player()
        self.enemy = Enemy()

    def __greet(self):
        print('Добро подаловать в Игру "Морской бой"!')
        print("Для начала необходимо выставить корабли.")
        # self.player.set_ships()
        self.enemy.set_ships()
        self.enemy.field.draw_field()
        print("Перед Вами два поля. Слева Ваше. Справа противника.")
        print("Для выстрела, введите координаты стрельбы Y X через пробел")

    def __loop(self):
        game = True
        while game:
            # self.player.draw_both_field()
            if self.player.shot(self.enemy.field):
                print('Попадание!')
            else:
                print('Промах!')
            if self.enemy.check_down_ship():
                print('Корабль противника Потоплен! Так держать!')
            if self.enemy.shot(self.player.field):
                print('В Ваш корабль попали!')
            else:
                print('Противник промахнулся!')
            if self.player.check_down_ship():
                print('Ваш корабль затонул!')
            if self.player.check_defeat():
                print('Все ваши корабли потоплены. Поражение!')
                game = False
            if self.enemy.check_defeat():
                print('Все корабли противника потоплены. Поздравляю с победой!')
                game = False

    def start(self):
        self.__greet()
        self.__loop()


