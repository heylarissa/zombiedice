from curses.ascii import isdigit
import random

class Dice:
    def __init__(self):
        """
        C: Cérebro
        P: passos
        T: tiro
        """

        self.greenDices = "CPCTPC" # 6
        self.yellowDices = "TPCTPC" # 4
        self.redDices = "TPTCPT" # 3

    def returnDices(quantity, dices_string):
        diceList = []
        for i in quantity:
            s = random.choice(dices_string)
            diceList.append(s)
        pass

    def threeShotguns(self):
        return

    def rollDices(self):

        return

    def isFootprint(self):
        return

    def isShotgun(self):
        return

    def isBrain(self):
        return


class Game:
    def __init__(self, players):
        self.turns = 0
        self.brains = 0
        self.status = True # True : Continue | False : Stop
        self.over = False
        self.players = self.initPlayers(players)
        pass

    def initPlayers(self, players):
        for i in range(players):
            
            pass
        pass
    def nextPlayer(self):
        return

    def selectPlayer(self):
        """ seleciona aleatoriamente o player """
        return

    def saveScore(self, newBrains):
        self.brains += newBrains

    def playerHas13Brains(self):
        return

    def keepGoing(self):
        return
    def setStatus (self, status):
        if status == 1:
            self.status = False
        elif status == 2:
            self.status = True
        else:
            print ("Should be 1 or 2")

    def printScreen(self):
        return

def main():
    players = int(input ("Number of Players: " ))
    while ((players < 2)):
        print ("The number of players should be 2 or more")

        players = int(input ("Number of Players: " ))

    dices = Dice()
    game = Game(players)

    while (not game.over):
        
        game.selectPlayer()
        dices.rollDices()
        newBrains = 0

        if (dices.isShotgun()):
            pass

        if (dices.isBrain()):
            newBrains+=1

        if (dices.threeShotguns):
            game.selectPlayer()
        
        if (dices.isFootprint()):
            if (game.keepGoing()):
                pass
            else:
                game.saveScore(newBrains)
                
        game.setStatus(int(input ("Press 1 to Stop or 2 to keep going ")))
        if (game.playerHas13Brains()):
            return game.over

        game.turns+=1

if __name__ == "__main__":
    main()