'''
Black Jack Game (Simplified)

1. 52 Card Deck - shuffled and ready to play.
2. Two Players - Human vs Computer
3. Start with drawing 4 Cards from the Deck. Two with Human player and two with Computer.
4. Human can see all cards in hand but can only see one card of the Computer.
5. Human is given a chance to either Hit or Stay. Hit = Draw an additional card from the Deck. Stay = Pass and it is not Computer's turn.
6. Computer will decide to Hit or Stay depending on the current value of the cards in hand. This version uses 17 but we can adjust this value.
7. Game Over Conditions:
	1. If the total value of the cards > 21, Game is over and the player loses the game.
	2. If the total value is <=21, whoever has the highest value wins.

Note: Ace has a value of 1 and Jack,Queen,King have a value of 10.
'''
import sys
import pdb
from random import shuffle

suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
ranks = ['Ace','Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
values = dict(zip(ranks,range(1,14)))
values['Jack'] = values['Queen'] = values['King'] = 10

class Card():

	'''
	Instantiate card by specifying suit and rank.
	Example: Card('Spades','Ace')
	'''

	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank
		self.value = values[self.rank]

	def __str__(self):
		return f'{self.rank} of {self.suit}'

class Deck():
	'''
	Instantiate a deck of 52 playing cards
	'''

	def __init__(self):
		self.allcards = []
		for suit in suits:
			for rank in ranks:
				card = Card(suit,rank)
				self.allcards.append(card)

	def shuffle(self):
		'''
		Shuffle the deck of playing cards
		'''
		return shuffle(self.allcards)

	def deal_one(self):
		return self.allcards.pop()

	def __str__(self):
		return f'This is a deck of playing cards'


class Player():
	'''
	Instantiate player to play the game.
	'''
	def __init__(self,name,chips=500):
		self.name = name
		self.cardsinhand = []
		self.chips = chips

	def hand(self):
		return self.cardsinhand

	def add_card(self,cards):
		if cards == type([]):
			self.cardsinhand.extend(cards)
		else:
			self.cardsinhand.append(cards)

	def totval(self):
		value = 0
		for card in self.cardsinhand:
			value += card.value
		return value

	def __str__(self):
		return f'Player: {self.name} has {self.chips} number of chips remaining'

def game_start():
	game_on = False
	print('\n' + '*'*50)
	print(' WELCOME TO BLACKJACK '.center(50,'*'))
	print('*'*50 + '\n')
	choice = input("\nDo you want to start the Game? Type 'Y' to start the game and any other key to exit:  " )
	if choice[0].lower() == 'y':
		name = input('\nPlayer 1, Enter your name: ')
		while True:
			try:
				chips = int(input('\nEnter the number of chips you would like to buy (in numbers) [Minimum: 500, Maximum: 5000]: '))
			except:
				print('Invalid choice! Please enter a number.')
			else:
				if chips < 500 or chips > 5000:
					print('Chips are outside the acceptable range! Please enter a value between 500 and 5000 ')
				else:
					break

		game_on = True
		return name,chips,game_on
	else:
		print('Good Bye!')
		sys.exit()

def show_cards():
	print('*'*29)
	print(f'{player1.name}, your cards are: ')
	print('-'*23)
	for cards in player1.cardsinhand:
		print('==> ' + str(cards))
	print('-'*29)
	print(f'Total value of the cards: {player1.totval()}')
	print('-'*29)
	print('*'*29)
	print('\n' + '*'*47)
	print(f'The cards of {player2.name} are: {player2.cardsinhand[0]}')
	print('*'*47 + '\n')

def show_cards_final():
	print('\n' + '*'*29)
	print(f'The cards of {player2.name} were: ')
	for cards in player2.cardsinhand:
		print('==> ' + str(cards))
	print('-'*29)
	print(f'Total value of the cards: {player2.totval()}')
	print('-'*29)
	print('*'*29 + '\n')

def play_again():
	choice = input('Press Y if you would like to play again: ')
	if choice[0].lower() == 'y':
		return True
	else:
		print(f'\n{player1.name} Chips: {player1.chips}\n')
		print('Good Bye!\n')
		return False

# CORE GAME LOOP

#Display Welcome Screen and ask if the Player wants to start the game.
p1_name,chips,game_on = game_start()
player1 = Player(p1_name,chips)
player2 = Player('Computer',chips)

##########################################################
# TEST Initializing variables to check core gameplay loop
# player1 = Player('alpha')
# player2 = Player('bravo')
# game_on = True
##########################################################

while game_on:

	print(f'\n{player1.name} Chips: {player1.chips}\n')

	if player1.chips == 0:
		print('Insufficient Balance! Please buy chips to Play!\n')
		break

	#Initialize and shuffle the card deck
	deck = Deck()
	deck.shuffle()

	#Initialize hands
	player1.cardsinhand = []
	player2.cardsinhand = []

	#Deal 4 cards from the Deck and assign to Player 1 and Player 2
	for num in range(2):
		player1.add_card(deck.deal_one())
		player2.add_card(deck.deal_one())

	#Show cards to Player
	show_cards()

	#Ask how much player wants to bet. It should not exceed the number of chips customer has.
	while True:
		try:
			betamount = int(input('Enter the Bet amount (in numbers): '))
		except:
			print('Please enter a valid amount!')
		else:
			if betamount <= player1.chips:
				player1.chips -= betamount
				print(f'Current Balance: {player1.chips}')
				break
			else:
				print('Insufficient Balance!')

	#Ask Player 1 if they want to Hit or Stay
	hit = True
	while hit and player1.totval() <= 21:			
		choice = input("Do you want to Hit or Stay? Press 'H' to hit or anything else to stay: ")
		if choice[0].lower() == 'h':
			player1.add_card(deck.deal_one())
			show_cards()
		else:
			print('You have chosen to Stay, passing over the control to Player 2.')
			hit = False
			break
	if player1.totval() > 21:
		print(f'\n{player1.name} is BUST!!\n{player2.name} WON!!!')
		show_cards_final()
		if play_again():
			continue
		else:
			game_on = False
			break

	#Player 2 turn
	print(f'\n{player2.name}`s Turn\n')

	# If total value of Player2 cards is less or equal to 17, keep drawing more cards from the deck.
	while player2.totval() < 17:
		player2.add_card(deck.deal_one())
		print(f'\n{player2.name} has drawn a card from the deck\n')

	if player2.totval() > 21:
		print(f'\n{player2.name} is BUST!!\n{player1.name} WON!!!')
		player1.chips += 2*betamount
		show_cards_final()
		if play_again():
			continue
		else:
			game_on = False
			break

	# Check for Win Condition if no player is BUST

	if player1.totval() > player2.totval():

		print(f'\n{player1.name} WON!!')
		show_cards_final()
		player1.chips += 2*betamount
		if play_again():
			continue
		else:
			break
	elif player1.totval() < player2.totval():
		print(f'\n{player2.name} WON!!')
		show_cards_final()
		if play_again():
			continue
		else:
			break
	else:
		print('DRAW!')
		show_cards_final()
		if play_again():
			continue
		else:
			break
