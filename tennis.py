# -*- coding: utf-8 -*-
class Game:
    zeroPoints = "Love"
    fifteenPoints = "Fifteen"
    thirtyPoints = "Thirty"
    fortyPoints = "Forty"
    moreThanThirtyPoints = "Deuce"
    tie = "-All"

    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0


    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.P1Score()
        else:
            self.P2Score()

    def score(self):
        result = ""
        if self.tieWithLessThanThreeHits():
            if self.playerWithoutPoints():
                result = self.zeroPoints
            if self.playerHasFifteenPoints():
                result = self.fifteenPoints
            if self.playerHasThirtyPoints():
                result = self.thirtyPoints
            result += self.tie
        if self.tieWithMoreThanTwoHits():
            result = self.moreThanThirtyPoints

        P1res = ""
        P2res = ""
        if self.onlyPlayerOneScored():
            P1res = self.playerOnePoints()
            P2res = self.zeroPoints
            result = P1res + "-" + P2res
        else:
            if self.onlyPlayerTwoScored():
                P2res = self.playerTwoPoints()
                P1res = self.zeroPoints
                result = P1res + "-" + P2res

        if self.playerOneWinningWithLessThanFourHits():
            if (self.p1points == 2):
                P1res = "Thirty"
            if (self.p1points == 3):
                P1res = "Forty"
            if (self.p2points == 1):
                P2res = "Fifteen"
            if (self.p2points == 2):
                P2res = "Thirty"
            result = P1res + "-" + P2res

        if self.playerTwoWinningWithLessThanFourHits():
            if (self.p2points == 2):
                P2res = "Thirty"
            if (self.p2points == 3):
                P2res = "Forty"
            if (self.p1points == 1):
                P1res = "Fifteen"
            if (self.p1points == 2):
                P1res = "Thirty"
            result = P1res + "-" + P2res

        if self.matchPointForPlayerOne():
            result = "Advantage " + self.player1Name

        if self.matchPointForPlayerTwo():
            result = "Advantage " + self.player2Name

        if self.playerOneWins():
            result = "Win for " + self.player1Name

        if self.playerTwoWins():
            result = "Win for " + self.player2Name
        return result

    def SetP1Score(self, number):
        for i in range(number):
            self.P1Score()

    def SetP2Score(self, number):
        for i in range(number):
            self.P2Score()

    def P1Score(self):
        self.p1points += 1

    def P2Score(self):
        self.p2points += 1

    def tieWithLessThanThreeHits(self):
        if self.p1points == self.p2points and self.p1points < 3:
            return True

    def playerWithoutPoints(self):
        if self.p1points == 0:
            return True

    def playerHasFifteenPoints(self):
        if self.p1points == 1:
            return True

    def playerHasThirtyPoints(self):
        if self.p1points == 2:
            return True

    def tieWithMoreThanTwoHits(self):
        if self.p1points == self.p2points and self.p1points > 2:
            return True

    def onlyPlayerOneScored(self):
        if self.p1points > 0 and self.p2points == 0:
            return True

    def onlyPlayerTwoScored(self):
        if self.p2points > 0 and self.p1points == 0:
            return True

    def playerOneWinningWithLessThanFourHits(self):
        if self.p1points > self.p2points and self.p1points < 4:
            return True

    def playerTwoWinningWithLessThanFourHits(self):
        if self.p2points > self.p1points and self.p2points < 4:
            return True

    def matchPointForPlayerOne(self):
        if self.p1points > self.p2points and self.p2points >= 3:
            return True

    def matchPointForPlayerTwo(self):
        if self.p2points > self.p1points and self.p1points >= 3:
            return True

    def playerOneWins(self):
        if self.p1points >= 4 and self.p2points >= 0 and (self.p1points - self.p2points) >= 2:
            return True

    def playerTwoWins(self):
        if self.p2points >= 4 and self.p1points >= 0 and (self.p2points - self.p1points) >= 2:
            return True

    def playerOnePoints(self):
        P1res = ""
        if self.p1points == 1:
            P1res = self.fifteenPoints
        if self.p1points == 2:
            P1res = self.thirtyPoints
        if self.p1points == 3:
            P1res = self.fortyPoints
        return P1res

    def playerTwoPoints(self):
        P2res = ""
        if (self.p2points == 1):
            P2res = self.fifteenPoints
        if (self.p2points == 2):
            P2res = self.thirtyPoints
        if (self.p2points == 3):
            P2res = self.fortyPoints
        return P2res
