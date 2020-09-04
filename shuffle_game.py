game_list = ['','O','']
from random import shuffle
###shuffling the list
def shuffle_list(game_list):
	shuffle(game_list)
	return game_list
shuffle_list(game_list)

####function for player guess
def player_guess():
	guess = ''
	while guess not in ['0','1','2']:
		  guess = input("Guess your place of '0' :")
		  return int(guess)
def check_guess(game_list,guess):
	if (game_list[guess] == 'O'):
		print ("Correct Guess")
		print(game_list)
	else:
		print("Wrong Guess")
		print(game_list)
###intialize the list
game_list = ['','O','']
###calling shuffle list function
shuffling_list = shuffle_list(game_list)
###calling player_guess function
guess = player_guess()
###calling check_guess function
check_guess(shuffling_list,guess)