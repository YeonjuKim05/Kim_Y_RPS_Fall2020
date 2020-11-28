# import packages to extend python (just like we extend sublime, or Atom, or VSCode)
from random import randint
from gameComponents import gameVars, chooseWinner



while gameVars.player is False:
	print("=======================*/ RPS CONTEST /*=======================")
	print("Computer Lives: ", gameVars.ai_lives, "/", gameVars.total_lives)
	print("Player Lives: ", gameVars.player_lives, "/", gameVars.total_lives)
	print("==============================================")

	print("Choose your weapon! or type quit to leave\n") 
	gameVars.player = input("Choose rock, paper or scissors: \n")

	# if the player chose to quit then exit the game
	if gameVars.player == "quit":
		print("You chose to quit")
		exit()

	#player = True -> it has a value (rock, paper, or scissors)
	
	# this will be the AI choice -> a random pick from the choices array
	computer = gameVars.choices[randint(0, 2)]

	# check to see what the user input

	# print outputs whatever is in the round brackets -> in this case it outputs player to the command prompt window
	print("user chose: " + gameVars.player)

	# validate that the random choice worked for the AI
	print("AI chose: " + computer)

	if (computer == gameVars.player):
		print("tie")

	# always check for negative conditions first (the losing case)

	elif (computer == "rock"):
		if (gameVars.player == "scissors"):
			print("you lose")
			gameVars.player_lives -= 1
		else:
			print("you win!")
			gameVars.ai_lives -= 1

	elif (computer == "paper"):
		if (gameVars.player == "rock"):
			print("you lose")
			gameVars.player_lives -= 1
		else:
			print("you win!")
			gameVars.ai_lives -= 1

	elif (computer == "scissors"):
		if (gameVars.player == "paper"):
			print("you lose")
			gameVars.player_lives -= 1
		else:
			print("you win!")
			gameVars.ai_lives -= 1





		#--------- stop here - all of the above needs to move ----------

	if gameVars.player_lives is 0:
		chooseWinner.winorlose("lost")

	if gameVars.ai_lives is 0:
		chooseWinner.winorlose("won")


	print("Player has", gameVars.player_lives, "lives left")
	print("AI has", gameVars.ai_lives, "lives left")


	gameVars.player = False


