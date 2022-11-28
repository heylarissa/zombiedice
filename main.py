import random
from time import sleep


class Dice:
    def __init__(self):

        """

        C: Cérebro
        P: passos
        T: tiro

        """

        self.greenDices = "CPCTPC"
        self.yellowDices = "TPCTPC"
        self.redDices = "TPTCPT"

        self.all13Dices = [
            self.greenDices,
            self.greenDices,
            self.greenDices,
            self.greenDices,
            self.greenDices,
            self.greenDices,
            self.yellowDices,
            self.yellowDices,
            self.yellowDices,
            self.yellowDices,
            self.redDices,
            self.redDices,
            self.redDices,
        ]
        self.currentDices = []  # lista os três últimos dados lançados
        self.rolledDices = []  # lista com todos os dados lançados

    def setDice(self, quantity, dices_string):

        diceList = []

        for i in range(quantity):
            s = random.choice(dices_string)
            diceList.append(s)

        return diceList

    def threeShotguns(self):
        return False

    def getThreeDices(self):
        dices = []
        if len(self.all13Dices) > 3:
            for i in range(3):
                sorted = random.randint(0, len(self.all13Dices) - 1)

                sortedDice = self.all13Dices.pop(sorted)
                dices.append(sortedDice)

                if sortedDice == self.greenDices:
                    print("Dado " + str(i + 1) + " é verde")
                elif sortedDice == self.yellowDices:
                    print("Dado " + str(i + 1) + " é amarelo")
                elif sortedDice == self.redDices:
                    print("Dado " + str(i + 1) + " é vermelho")

            self.currentDices = dices
            del dices
        else:
            pass

    def rollDices(self):
        """rola os 3 dados sorteados"""
        print()
        print("As faces sorteadas foram: ")

        for i in range(len(self.currentDices)):
            sorted = random.randint(0, 5)
            self.rolledDices.append(self.currentDices[i][sorted])
            print("Dado " + str(i + 1) + ": " + self.currentDices[i][sorted])

        print()

    def isFootprint(self):
        return

    def isShotgun(self):
        return

    def isBrain(self):
        return


class Player:
    def __init__(self, id, name):
        """Inicializa o jogador"""
        self.turns = 0
        self.brains = 0
        self.id = id
        self.name = name


class Game:
    def __init__(self):
        """Inicializa o jogo"""
        self.turns = 0
        self.brains = 0
        self.status = True
        self.over = False
        self.playersNumber = int(input("Number of Players: "))
        self.players = self.initPlayers()
        self.currentPlayer = self.players[
            0
        ]  # primeiro jogador é o de posição 0 na lista players

    def initPlayers(self):
        players = []
        for i in range(self.playersNumber):
            name = input("Nome do jogador " + str(i) + ": ")
            newPlayer = Player(i, name)
            players.append(newPlayer)
        return players

    def selectNextPlayer(self):
        """seleciona o próximo player e
        atualiza o número de turnos jogados pelo jogador"""

        if self.turns >= 1 and self.status == False:
            self.currentPlayer.turns += 1
            self.players[self.currentPlayer.id] = self.currentPlayer

            id_next = self.currentPlayer.id + 1

            if (
                id_next == self.playersNumber
            ):  # se estiver no último jogador, volta para o primeiro
                id_next = 0

            self.currentPlayer = self.players[id_next]

    def saveScore(self, newBrains):
        self.brains += newBrains

    def playerWonGame(self):
        """verifica se o jogador tem 13 cérebros e se todos os jogadores jogaram o mesmo número de turnos"""
        return

    def keepGoing(self):
        return

    def setStatus(self, status):
        """incrementa o número de turnos se trocar de jogador
        recebe o input do jogador e retorna se é válido"""

        if status == "1":
            self.status = False
            self.turns += 1
        elif status == "2":
            self.status = True
        else:
            print("Should be 1 or 2")
            exit()

    def printScreen(self):
        print()
        print("Turno: " + str(self.turns))
        print("Jogador: " + str(self.currentPlayer.id))
        print(self.currentPlayer.name + ", é a sua vez!")


def main():
    game = Game()

    while game.playersNumber < 2:
        print("The number of players should be 2 or more")

        game.playersNumber = input("Number of Players: ")

    dices = Dice()

    while not game.over:
        game.printScreen()

        dices.getThreeDices()
        dices.rollDices()
        newBrains = 0

        if dices.isShotgun():
            pass

        if dices.isBrain():
            newBrains += 1

        if dices.threeShotguns():
            continue

        game.setStatus(input("Press 1 to Stop or 2 to keep going   "))

        if dices.isFootprint():
            if game.status == True:  # o turno continua
                dices.rollDices()

            else:  # se o jogador optou por parar, o próximo jogador é selecionado
                game.saveScore(newBrains)
                continue

        if game.playerWonGame():
            game.over = True

        game.selectNextPlayer()


if __name__ == "__main__":
    main()
