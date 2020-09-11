import random
import pdb
#initialization
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
#CARD
# SUIT,RANK,VALUE
class Card:

	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank
		self.value = values[rank]

	def __str__(self):
		return self.rank + "of" + self.suit
#Deck class for creating cards
class Deck:
	def __init__(self):
        # Note this only happens once upon creation of a new Deck
		self.allcards = [] 
		for suit in suits:
			for rank in ranks:
                # This assumes the Card class has already been defined!
				self.allcards.append(Card(suit,rank))
                
	def shuffle(self):
        # Note this doesn't return anything
		random.shuffle(self.allcards)
        
	def deal_one(self):
        # Note we remove one card from the list of allcards
		return self.allcards.pop()
#player class

class player:
	def __init__(self,name):
		self.name = name
		self.allcards = []

	#remove one
	def remove_one(self):
		return self.allcards.pop(0)

    #adding cards
	def add_cards(self,new_cards):
		if type(new_cards) == type([]):
			#multiple value or cards
			return self.allcards.extend(new_cards)
		else:
			#single card or one value
			return self.allcards.append(new_cards)


	def __str__(self):
		return f'player{self.name} has {len(self.allcards)} cards.'
#Game setup for two players
player_one = player("one")
player_two = player("two")
new_deck = Deck()
new_deck.shuffle()

for x in range(26):

	player_one.add_cards(new_deck.deal_one())

	player_two.add_cards(new_deck.deal_one())

#Game logic for War Game
game_on = True
round_num = 0
while game_on:
	round_num += 1
	print (f"Round{round_num}")

	if len(player_one.allcards) == 0:
		print("Player one is out of cards! player Two wins!")
		print("Game Over")
		game_on = False
		break


	if len(player_two.allcards) == 0:
		print("Player two is out of cards! player one wins!")
		print("Game Over")
		game_on = False
		break
	player_one_cards = []
	player_one_cards.append(player_one.remove_one())

	player_two_cards = []
	player_two_cards.append(player_two.remove_one())

	at_war = True

	while at_war:
		if player_one_cards[-1].value > player_two_cards[-1].value:

			#player one gets the card
			player_one.add_cards(player_one_cards)
			player_one.add_cards(player_two_cards)
			at_war = False
		elif player_one_cards[-1].value < player_two_cards[-1].value:
			#player 2 has higher card
			player_two.add_cards(player_one_cards)
			player_two.add_cards(player_two_cards)
			at_war = False
		else:
			print('WAR!')
			#this will occur when the both cards are same

			if len(player_one.allcards) < 5:
				print("player one unable to play war ! Game over")
				print("player two wins! player one loses")
				game_on = False
				break
			elif len(player_two.allcards) < 5:
				print("players two unable to play war! Game over")
				print("player one wins! player two loses")
				at_war = False
				break
			else:
				for num in range(5):
					player_one_cards.append(player_one.remove_one())
					player_two_cards.append(player_two.remove_one())