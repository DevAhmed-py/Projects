#Black Jack Game

from random import shuffle

print('WELCOME TO PLAY BLACK JACK')

def createDeck():

    Deck = []

    faceValue = ['A','J','Q','K']

    for i in range(4):
        for card in range(2,11):
            Deck.append(str(card))

        for cards in faceValue:
            Deck.append(cards)

    shuffle(Deck)
    return Deck

class Player:

    def __init__(self, Hand = [], money = 100):

        self.hand = Hand
        self.score = self.setScore()
        self.money = money
        self.bet = 0

    def __str__(self):

        currentHand = ''

        for card in self.hand:
            currentHand += card + ' '

        finalStatus = currentHand + 'score is: ' + str(self.score)

        return finalStatus

    def setScore(self):
        self.score = 0

        faceCardDict = {'A':11, 'J':10, 'Q':10, 'K':10, '2':2, '3':3,
                         '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10}

        aceCounter = 0
        for card in self.hand:
            self.score += faceCardDict[card]

            if card == 'A':
                aceCounter += 1
            if self.score > 21 and aceCounter != 0:
                self.score -= 10
                aceCounter -= 1

        return self.score

    def hit(self, card):
        self.hand.append(card)
        self.score = self.setScore()

    def play(self, newHand):
        self.hand = newHand
        self.score = self.setScore()

    def betMoney(self, amount):
        self.money -= amount
        self.bet += amount

    def win(self, result):
        if result == True:
            if self.score == 21 and len(self.hand) == 2:
                self.money += 2.5 * self.bet

            else:
                self.money += 2 * self.bet

            self.bet = 0
        else:
            self.bet = 0

    def draw(self):
        self.money += self.bet
        self.bet = 0

    def hasBlackJack(self):
        if self.score == 21 and len(self.hand) == 2:
            return True
        else:
            return False

            
def printHouse(House):

    for card in range(len(House.hand)):

        if card == 0:
            print('\nx', end = ' ')
        elif card == len(House.hand) - 1:
            print(House.hand[card])
        else:
            print(House.hand[card], end = ' ')

cardDeck = createDeck()
firstHand = [cardDeck.pop(),cardDeck.pop()]
secondHand = [cardDeck.pop(),cardDeck.pop()]

Player1 = Player(firstHand)
House = Player(secondHand)
cardDeck = createDeck()

while True:
    if len(cardDeck) < 20:
        cardDeck = createDeck()

    firstHand = [cardDeck.pop(),cardDeck.pop()]
    secondHand = [cardDeck.pop(),cardDeck.pop()]

    Player1 = Player(firstHand)
    House = Player (secondHand)

    Bet = int(input('\nPlease enter your bet: '))
    Player1.betMoney(Bet)

    print(cardDeck)
    printHouse(House)
    print('\n{}'.format(Player1))
    
    if Player1.hasBlackJack():
        
        if House.hasBlackJack():
            Player1.draw()
        else:
            Player1.win(True)
    else:
        
        while (Player1.score < 21):
            action = input('\nDo you want another card? (y/n)?: ')
            if action == 'y':
                Player1.hit(cardDeck.pop())
                print('\n{}'.format(Player1))
                printHouse(House)

            else:
                break
        while (House.score < 16):
            print(House)
            House.hit(cardDeck.pop())

        if Player1.score > 21:
            if House.score > 21:
                Player1.draw()
                print('\nit is a DRAW')
            else:
                Player1.win(False)
                print('\nPlayer1 LOST')

        elif Player1.score > House.score:
            Player1.win(True)
            print('\nPlayer1 WINS')

        elif Player1 == House.score:
            Player1.draw()
            print('\nit is a DRAW')

        else:
            if House.score > 21:
                Player1.win(True)
                print('\nPlayer1 WINS')

            else:
                Player1.win(False)
                print('\nPlayer1 LOST')


    print(House)
    print('\nCash Balance: ${}'.format(Player1.money))
    
