'''
WAR Game Rules (Simplified Version)

1. Start with a deck of 52 playing cards.
2. Distribute cards to players in equal halves - each player has 26 cards.
3. Every turn, Players will draw one card each from the top of their hand.
4. Player card with the highest value wins the round and takes both the cards and add them to the bottom of their hand.
5. In case the value of both cards is same, then we have a situation of WAR!.
6. The players will draw 5 cards each, 4 will be kept face-down and the 5th card will be face-up and used to compare the values.
7. The player card with the highest value wins the round and takes all the cards 'on-table' and add them to the bottom of their hand.
8. In case the value of 5th Card is also the same resulting in another War, the process of War will repeat unless we have a winner.
9. The Player will lose the Game if:
    a. They run out of playing cards.
    b. They have less than 5 cards at the start of War.
'''

from random import shuffle

#Global Variables
suits = ['Diamonds','Hearts','Aces','Clubs']
ranks = ['Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace']
values = dict(zip(ranks,range(2,15)))

# Cards Class
class Cards:
    '''
    Create an instance of a playing card.
    '''

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[self.rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'

# Deck Class
class Deck:
    '''
    Create a Deck of 52 cards.
    '''

    def __init__(self):
        self.allcards = []
        for suit in suits:
            for rank in ranks:
                mycard = Cards(suit,rank)
                self.allcards.append(mycard)

    def shuffle(self):
        '''
        Shuffle the Deck of cards.
        '''
        shuffle(self.allcards)

    def draw_one(self):
        '''
        Remove one card (last) from the Deck.
        '''
        return self.allcards.pop()

# Player Class
class Player:
    '''
    Instantiate player and allow the player to draw and pick cards to and from the table.
    '''

    def __init__(self,name):
        self.name = name
        #Index 0 is the top of the hand and -1 is the bottom
        self.cardsinhand = []

    def draw_one(self):
        #Draw one card from the top of the hand
        return self.cardsinhand.pop(0)

    def add_cards(self,addcards):
        #This method will add cards to the bottom of the hand.
        #Extend the list if addcards is a list
        if type(addcards) == type([]):
            self.cardsinhand.extend(addcards)
        #Append to the list if addcards is a single card
        else:
            self.cardsinhand.append(addcards)

    def __str__(self):
        return f'Player {self.name} has {len(self.cardsinhand)} cards'


# Intantiate and Shuffle the Card deck
newdeck = Deck()
newdeck.shuffle()

# Instantiate players
player1 = Player('Player_1')
player2 = Player('Player_2')

# Distribute cards from card deck to both Players
for num in range(26):
    player1.add_cards(newdeck.draw_one())
    player2.add_cards(newdeck.draw_one())

game_on = True
counter = 0

# Game Start
while game_on:
    counter += 1
    print(f'Round Number: {counter}')

    #Check if Player1 or Player2 has run out of cards.
    if len(player1.cardsinhand) == 0:
        print(f'GAME OVER!\nPlayer_1 has 0 cards remaining.\nPlayer_2 WON!!!')
        game_on = False
        break
    elif len(player2.cardsinhand) == 0:
        print(f'GAME OVER!\nPlayer_2 has 0 cards remaining.\nPlayer_1 WON!!!')
        game_on = False
        break

    #If both players have cards in their hand, we will start with Game Round.
    #The cards on-table will be 0 at the beginning of each round.
    #Each Player will draw one card from the top of their hand.

    player1_cards_on_table = []
    player1_cards_on_table.append(player1.draw_one())

    player2_cards_on_table = []
    player2_cards_on_table.append(player2.draw_one())

    at_war = True

    while at_war:
        #If Player1 card value > Player2 card value, Player1 takes all the cards and we are not at WAR
        if player1_cards_on_table[-1].value > player2_cards_on_table[-1].value:
            player1.add_cards(player1_cards_on_table)
            player1.add_cards(player2_cards_on_table)
            at_war = False
        #If Player1 card value < Player2 card value, Player2 takes all the cards and we are not at WAR
        elif player1_cards_on_table[-1].value < player2_cards_on_table[-1].value:
            player2.add_cards(player1_cards_on_table)
            player2.add_cards(player2_cards_on_table)
            at_war = False
        #This condition will be met if we are at War.
        else:
            print('WAR!!!')
            #Check if both Players have enough cards to play.
            if len(player1.cardsinhand) < 5:
                print('GAME OVER! Player1 does not have enough cards to play War!\nPlayer2 WON!!!')
                at_war = False
                game_on = False
                break
            elif len(player2.cardsinhand) < 5:
                print('GAME OVER! Player2 does not have enough cards to play War!\nPlayer1 WON!!!')
                at_war = False
                game_on = False
                break
            #If both Players have enough cards to play, draw Five cards and append them to cards_on_table
            else:
                for num in range(5):
                    player1_cards_on_table.append(player1.draw_one())
                    player2_cards_on_table.append(player2.draw_one())
