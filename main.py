import random

class Dice:
    def __init__(self):
        """
        C: Cérebro
        P: passos
        T: tiro
        """

        self.greenDices = self.setDice(6, "CPCTPC")
        self.yellowDices = self.setDice(4, "TPCTPC")
        self.redDices = self.setDice(3, "TPTCPT")

        self.currentDices = () # tupla que atualiza com os últimos dados lançados

    def setDice (self, quantity, dices_string):
        diceList = []
        for i in range(quantity):
            s = random.choice(dices_string)
            diceList.append(s)
        return diceList

    def threeShotguns(self):
        return False

    def rollDices(self):
        return

    def isFootprint(self):
        return

    def isShotgun(self):
        return

    def isBrain(self):
        return

class Player:
     
    def __init__(self, id):
        self.turns = 0
        self.brains = 0
        self.id = id

class Game:
    def __init__(self):
        self.turns = 0
        self.brains = 0
        self.status = True
        self.over = False
        self.playersNumber = int(input ("Number of Players: " ))
        self.players = self.initPlayers()
        self.currentPlayer = self.players[0] # primeiro jogador é o de posição 0 na lista players

    def initPlayers(self):
        players = []
        for i in range (self.playersNumber):
            newPlayer = Player(i)
            players.append(newPlayer)
        return players

    def selectNextPlayer(self):
        """ seleciona o próximo player e 
        atualiza o número de turnos jogados pelo jogador """

        if (self.turns >= 1 and self.status == False):
            self.currentPlayer.turns+=1
            self.players[self.currentPlayer.id] = self.currentPlayer

            id_next = self.currentPlayer.id + 1

            if id_next == self.playersNumber: # se estiver no último jogador, volta para o primeiro
                id_next = 0
            
            self.currentPlayer = self.players[id_next]

    def saveScore(self, newBrains):
        self.brains += newBrains

    def playerWonGame(self):
        """ verifica se o jogador tem 13 cérebros e se todos os jogadores jogaram o mesmo número de turnos """
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
        print("turno " + str(self.turns))
        print("jogador " + str(self.currentPlayer.id))

def main():
    game = Game()

    while ((game.playersNumber < 2)):
        print ("The number of players should be 2 or more")

        game.playersNumber = int(input ("Number of Players: "))

    dices = Dice()

    while (not game.over):
        game.printScreen()
        
        dices.rollDices()
        newBrains = 0

        if (dices.isShotgun()):
            pass

        if (dices.isBrain()):
            newBrains+=1

        if (dices.threeShotguns()):
            continue
        
        game.setStatus(int(input("Press 1 to Stop or 2 to keep going   ")))

        if (dices.isFootprint()):
            if (game.status == True):
                dices.rollDices()
                pass
            else:               # se o jogador optou por parar, o próximo jogador é selecionado
                game.saveScore(newBrains)
                continue

        if (game.playerWonGame()):
            game.over = True

        game.turns+=1
        game.selectNextPlayer()

if __name__ == "__main__":
    main()