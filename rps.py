##Simple rock-paper-scissors game to play with computer##
from random import randint

#initial variables
player1, computer="", ""
player_wins, computer_wins=0, 0
number=0


print('*ROCK*\n**PAPER**\n***SCISSORS***\n')
number=int(input("How many won rounds wins the game?\n"))

#main loop
while True:
	player1=input('\nPlease enter Player\'s choice (r for rock, p for paper, s for scissors):\n').lower()
    
	if player1=='q':
		break
	elif player1 not in 'rps':
		player1='lost'
		print("\nINVALID CHOICE!!!\n")
	computer='rps'[randint(0,2)] #computer choice

    #round result determination
	if player1=='lost':
		print('YOU LOST!!\n')
		computer_wins+=1
	elif player1==computer:
		print('\nComputer plays the same as you!')
		print('DRAW!\n')
	elif player1=='r':
		if computer=='p':
			print('\nComputer plays paper')
			print('COMPUTER WINS THIS ROUND!\n')
			computer_wins+=1
		else:
			print('\nComputer plays scissors!')
			print('PLAYER WINS THIS ROUND!\n')
			player_wins+=1
	elif player1=='p':
		if computer=='s':
			print('\nComputer plays scissors!')
			print('COMPUTER WINS THIS ROUND!\n')
			computer_wins+=1
		else:
			print('\nComputer plays rock')
			print('PLAYER WINS THIS ROUND!\n')
			player_wins+=1
	elif player1=='s':
		if computer=='r':
			print('\nComputer plays rock')
			print('COMPUTER WINS THIS ROUND!\n')
			computer_wins+=1
		else:
			print('\nComputer plays paper')
			print('PLAYER WINS THIS ROUND!\n')
			player_wins+=1

	print(f"#####Current score: Player - Computer {player_wins}:{computer_wins}#####\n")

	if computer_wins==number:
		print("COMPUTER WINS THE GAME!!!\n")
		break
	elif player_wins==number:
		print("PLAYER WINS THE GAME!!!\n")
		break

print('KONIEC I BOMBA, KTO PRZEGRAŁ TEN TRĄBA!!!!')
