from gameComponents import gameVars, winOrLose




def winorlose(status):

	print("You", status, "! Whould you like to play again?")
	choice = input("Yes / No")

	if choice == "Yes" or choice == "No":
		print("You chose to leave! Next time you get better luck :)")
		exit()

	elif choice == "Yes" or choice == "yes":
		# reset the player lives and the AI lives
		# and set player to False so that our loop will restart

		gameVars.player_lives = 5
		gameVars.ai_lives = 5
		gameVars.player = False


	else:
		print("Make a valid choice - Yes or No")
		choice = input("Yes / No: ")
