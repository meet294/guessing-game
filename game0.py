print('Welcome to GUESS ME!')
print('In this game, I have selected a number from 1 to 100 and you have to guess that number')
print(' RULES: ')
print("1. If the number you guessed is within 10 didgits from my number, I'll say WARM! \n and if the number is not within the digits then I'll say COLD!")
print("2. If you guess my number you will win the game!")
print("Let's Begin!")




import random
my_guess = random.randint(0,100)
guesses = [0]

while True:

	choice = input('Please enter a digit(0-100)')

	if choice.isdigit() != True:
		print('please enter a valid digit.')
		continue

	if int(choice) not in range(0,101):
		print('please enter an in range digit.')
		continue



	if int(choice) == my_guess:
		print(f'Congratulations! you did it in {len(guesses)} guesses.')
		break

	guesses.append(choice)

	if guesses[-2]:
		if abs(my_guess-int(guesses[-2])) > abs(my_guess-int(choice)):
			print('WARMER')

		else:
			print('COLDER')

	else:
		if (-10)<=abs(int(choice)-my_guess)<= 10:
			print('WARM')
		else:
			print('COLD')
		