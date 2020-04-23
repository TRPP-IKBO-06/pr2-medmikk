from random import randint

class Game:
    def __init__(self, playrs):
         self._roles = []
         self._playrs = playrs
         self.num = 0

    def create_pool(self):
        if self._playrs >= 6 and self._playrs <= 8:
            self._roles = ["mir" for i in range(0, self._playrs - 3)]
            self._roles.append("mafia")
            self._roles.append("don")
            self._roles.append("detective")

        if self._playrs >= 9:
            self._roles = ["mir" for i in range(0, self._playrs - 4)]
            self._roles.append("mafia")
            self._roles.append("mafia")
            self._roles.append("don")
            self._roles.append("detective")

    def get_pool(self):
        print(self._roles)

class Player(Game):
    def __init__(self, other):
        self.__game_role = ""
        other.num  += 1

    def get_game_role(self, other):
        print("роль игрока номер: ", other.num, "  ", self.__game_role)

    def get_role(self, other):
        while True:
            temp = randint(0, other._playrs - 1)
            self.__game_role = other._roles[temp]
            if self.__game_role != " ":
                other._roles[temp] = " "
                break
