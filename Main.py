from Game import Game


class Main:
    def __init__(self):
        self._game = Game()
        self.menu()

    def menu(self):
        userInput = ""
        while(userInput != "x"):
            self._game.printBoard()
            print()
            userInput = input("w, a, s, d eller x for å avslutte\n")
            if(userInput == "w" or userInput == "a" or userInput == "s" or userInput == "d"):
                self._game.move(userInput)


main = Main()
