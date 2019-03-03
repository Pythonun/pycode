import random
def roll_dice(numbers = 3,points = None):
	print('<<<<<<< ROLL THE DICE >>>>>>>>')
	if points is None:
		point = []
	while numbers > 0:
		point = random.randrange(1,7)
		points.append(point)
		numbers = numbers - 1
	return points

def roll_result(total):
	isBig = 11 < total < 18
	isSmall = 3 < total < 10
	if isBig:
		return 'Big'
	elif isSmall:
		return 'Small'
	
def start_game():
	your_money = 1000
	while your_money > 0:
		print('<<<<<<< GAME STARTS! >>>>>>>')
		choices = ['Big','Small']
		your_choice = input('Big or Samll:')
		if your_choice in choices:
			your_bet = int(input('how much you wanna bet? - '))
			points = roll_dice()
			total = sum(points)
			youwin = your_choice == roll_result(total)
			if youwin:
				print('The points is',points,'youwin!')
				print('you gained {},you have {} now'.format(your_bet,your_money + your_bet))
			else:
				print('The points is',points,'youlose!')
				print('you lost {},you have {} now'.format(your_bet,your_money - your_bet))
				your_money = your_money - your_bet
		else:
			print('Invalid words')
	else:
		print('GAME OVER')
