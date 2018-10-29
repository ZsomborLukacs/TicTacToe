import os
import time
import random

def rules_multiplayer():
	print("""
	
Multiplayer rules:
	Janika
Each player choose a character.

To choose a field, players should enter a number from 1 to 9.

The player who succeeds in placing three of their chosen character in a 
horizontal, vertical, or diagonal row wins the game.
	
	""")

def rules_single_player():
	print("""

Single player rules:

Player plays against computer.

To choose a field player should enter a number from 1 to 9.

Place three of your character in a horizontal, vertical, or diagonal row to win.
	""")


def result_printing_single_player(Player_1, Computer, Draw):
	print("")
	print("Result:")
	print("")
	print("Player 1: ", Player_1)
	print("Computer: ", Computer)
	print("Draw: ", Draw)

def result_printing_multiplayer(Player_1, Player_2, Draw):
	print("")
	print("Result:")
	print("")
	print("Player 1: ", Player_1)
	print("Player 2: ", Player_2)
	print("Draw: ", Draw)


def menu_printing():
	print("""
Welcome to Tic Tac Toe!

PLease choose:

1. Single player
2. Multiplayer
3. Quit
""")


def board_printing():

	print (" _____ _____ _____")
	print ("|     |     |     |")
	print ("|  "+board[1]+"  |  "+board[2]+"  |  "+board[3]+"  |")
	print ("|_____|_____|_____|")
	print ("|     |     |     |")
	print ("|  "+board[4]+"  |  "+board[5]+"  |  "+board[6]+"  |")
	print ("|_____|_____|_____|")
	print ("|     |     |     |")
	print ("|  "+board[7]+"  |  "+board[8]+"  |  "+board[9]+"  |")
	print ("|_____|_____|_____|")

board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

menu_printing()

Menu = int(input())

single_Player_Score = 0
computer_Score = 0
single_player_draw = 0

player_1_Score = 0
player_2_Score = 0
draw_Score = 0

while True:
	board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
	if(Menu == 1):
		
		rules_single_player()
		print("Choose a character: ")
		player1_Character = input()

		print("Choose AI character: ")
		ai_Character = input()

		counter = 1

		while True:
			os.system("clear")
			board_printing()
			if (counter % 2 == 1):
				choice = input("Player's turn: ")
				choice = int(choice)
				current_Player_Character = player1_Character
			else:
				print("Computer's turn: ")
				choice = int(random.randint(1,9))
				while(board[choice] != " "):
					choice = int(random.randint(1,9))
				current_Player_Character = ai_Character


			if (board[choice] == " "):
				board[choice] = current_Player_Character
				counter += 1
			else:
				print ("Sorry, that's not an empty place!")
				time.sleep(3)

			if (board[1] == current_Player_Character and board[2] == current_Player_Character and board[3] == current_Player_Character) or \
				(board[4] == current_Player_Character and board[5] == current_Player_Character and board[6] == current_Player_Character) or \
				(board[7] == current_Player_Character and board[8] == current_Player_Character and board[9] == current_Player_Character) or \
				(board[1] == current_Player_Character and board[4] == current_Player_Character and board[7] == current_Player_Character) or \
				(board[2] == current_Player_Character and board[5] == current_Player_Character and board[8] == current_Player_Character) or \
				(board[3] == current_Player_Character and board[6] == current_Player_Character and board[9] == current_Player_Character) or \
				(board[1] == current_Player_Character and board[5] == current_Player_Character and board[9] == current_Player_Character) or \
				(board[3] == current_Player_Character and board[5] == current_Player_Character and board[7] == current_Player_Character):
				os.system("clear")
				
				if(current_Player_Character == player1_Character):
					print ("Player won, congratulations!")
					single_Player_Score += 1
				if(current_Player_Character == ai_Character):
					print("Computer won!")
					computer_Score += 1
				
				board_printing()
				result_printing_single_player(single_Player_Score, computer_Score, draw_Score)

				break
			
			if (counter == 10):

				print("It's a draw.")
				single_player_draw += 1
				
				board_printing()				
				result_printing_single_player(single_Player_Score, computer_Score, draw_Score)

				break
	
	if(Menu == 2):

		rules_multiplayer()
		print("First player choose a character: ")
		player1_Character = input()

		print("Second player choose a character: ")
		player2_Character = input()

		counter = 1

		while True:
			os.system("clear")
			board_printing()
			if (counter % 2 == 1):
				choice = input("First player's turn: ")
				choice = int(choice)
				current_Player_Character = player1_Character
			else:
				choice = input("Second player's turn: ")
				choice = int(choice)
				current_Player_Character = player2_Character


			if (board[choice] == " "):
				board[choice] = current_Player_Character
				counter += 1
			else:
				print ("Sorry, that's not an empty place!")
				time.sleep(3)

			if (board[1] == current_Player_Character and board[2] == current_Player_Character and board[3] == current_Player_Character) or \
				(board[4] == current_Player_Character and board[5] == current_Player_Character and board[6] == current_Player_Character) or \
				(board[7] == current_Player_Character and board[8] == current_Player_Character and board[9] == current_Player_Character) or \
				(board[1] == current_Player_Character and board[4] == current_Player_Character and board[7] == current_Player_Character) or \
				(board[2] == current_Player_Character and board[5] == current_Player_Character and board[8] == current_Player_Character) or \
				(board[3] == current_Player_Character and board[6] == current_Player_Character and board[9] == current_Player_Character) or \
				(board[1] == current_Player_Character and board[5] == current_Player_Character and board[9] == current_Player_Character) or \
				(board[3] == current_Player_Character and board[5] == current_Player_Character and board[7] == current_Player_Character):
				os.system("clear")

				print (current_Player_Character, " wins! Congratulations")
				board_printing()
				if (counter % 2 == 1):
					player_2_Score += 1
				if (counter % 2 == 0):
					player_1_Score += 1

				result_printing_multiplayer(player_1_Score, player_2_Score, draw_Score)
				break
			
			if (counter == 10):

				print("It's a draw.")
				board_printing()
				draw_Score += 1

				result_printing_multiplayer(player_1_Score, player_2_Score, draw_Score)
				break
	
	if(Menu == 3):

		print("Would you like to save results? (y/n)")
		save = input()
		if(save == "y"):
			print("Select a name for the current results: ")
			save_name = input()

			single_Player_Score_str = str(single_Player_Score)
			computer_Score_str = str(computer_Score)
			single_player_draw_str = str(single_player_draw)

			player_1_Score_str = str(player_1_Score)
			player_2_Score_str = str(player_2_Score)
			draw_Score_str = str(draw_Score)
			
			try:
				file = open("Save.txt", "a")
				file.write(save_name)
				file.write('\n')
				file.write('\n')
				file.write("Result:")
				file.write('\n')
				file.write('\n')
				file.write("Single player results:")
				file.write('\n')
				file.write('\n')
				file.write("Player score:   ")
				file.write(single_Player_Score_str)
				file.write('\n')
				file.write("Computer score: ")
				file.write(computer_Score_str)
				file.write('\n')
				file.write("Draw score:     ")
				file.write(single_player_draw_str)
				file.write('\n')
				file.write('\n')
				file.write("Multiplayer results:")
				file.write('\n')
				file.write('\n')
				file.write("Player 1 score:     ")
				file.write(player_1_Score_str)
				file.write('\n')
				file.write("Player 2 score:     ")
				file.write(player_2_Score_str)
				file.write('\n')
				file.write("Draw score:         ")
				file.write(draw_Score_str)
				file.write('\n')
				file.write('\n')
				file.write('\n')


				print("Results saved.")

				file.close()
			except:
				print("Writing error")

			
			print("Thanks for playing, hope you had a good time!")
		if(save == "n"):
			print("Thanks for playing, hope you had a good time!")
		break
	
	Second_input = int(input("What would you like to do? (1: Rematch, 2: Main menu)"))

	if(Second_input == 1 and Menu == 1):
		Menu = 1

	if(Second_input == 1 and Menu == 2):
		Menu = 2
		
	if(Second_input == 2):
		menu_printing()
		Menu = int(input())