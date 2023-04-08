from player import Player
from enemy import Enemy

def main():
    print('Добро подаловать в Игру "Морской бой"!')
    print("Для начала необходимо выставить корабли.")
    player = Player()
    player.set_ships()
    enemy = Enemy()
    # enemy.set_ships()
    print("Перед Вами два поля. Слева Ваше. Справа противника.")
    print("Для выстрела, введите координаты стрельбы Y X через пробел")
    game = True
    while game:
        player.draw_both_field()
        # enemy.draw_both_field()
        if player.shot(enemy.field):
            print('Попадание!')
        else:
            print('Промах!')
        if enemy.check_down_ship():
            print('Корабль противника Потоплен! Так держать!')
        if enemy.shot(player.field):
            print('В Ваш корабль попали!')
        else:
            print('Противник промахнулся!')
        if player.check_down_ship():
            print('Ваш корабль затонул!')






if __name__ == '__main__':
    main()
