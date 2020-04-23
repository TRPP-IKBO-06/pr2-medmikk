from mafia import *

if __name__ == '__main__':
    num = int( input("Введите кол-во игроков: "))
    game = Game(num)
    game.create_pool()
    #game.get_pool()

    test = ["" for i in range(0, num)]
    for i in range(0, num):
        test[i] = Player(game)
        test[i].get_role(game)
        test[i].get_game_role(game)

    input("Enter something to exit")
