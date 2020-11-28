from gameComponents import gameVars




def winorlose(status):

	print("You", status, "! Whould you like to play again?")
	choice = input("Yes / No")

	if choice == "Yes" or choice == "No":
		print("You chose to leave! Next time you get better luck :)")
		exit()

	elif choice == "Yes" or choice == "yes":


		gameVars.player_lives = 1
		gameVars.ai_lives = 1
		gameVars.player = False


	else:
		print("Make a valid choice - Yes or No")
		choice = input("Yes / No: ")
