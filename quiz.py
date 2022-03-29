from operator import truediv


playing = input("Do you want to play? ")

if playing.lower() != "yes":
	quit()
x = 1
while x == 1:
	x = 1
	print("okay! let's play :)")
	score = 0

	answer = input("What does CPU stand for?")

	if answer.lower() == "central processing unit":
		print('Correct!')
		score +=1
	else:
		print('Incorrect!')

	answer = input("What does RAM stand for?")

	if answer.lower() == "random access memory":
		print('Correct!')
		score +=1
	else:
		print('Incorrect!')

	answer = input("What does PSU stand for?")

	if answer.lower() == "power supply unit":
		print('Correct!')
		score +=1
	else:
		print('Incorrect!')

	if score == 3:
		print(f"Congratulations! You got them all correct! score: {score}/3")
	else:
		print(f"Better luck next time! Score: {score}/3")
	
	play_again = input("Do you want to try again?")

	if play_again.lower() == "yes":
		x = 1
	else:
		x = 0
