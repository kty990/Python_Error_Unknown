import itertools
import string

use = []
attempt_num = []

def guess_password(real):
	chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
	attempts = 0
	for password_length in range(1, 9):
		for guess in itertools.product(chars, repeat=password_length):
			attempts += 1
			guess = ''.join(guess)
			print(guess)
			if guess == real:
				attempt_num.insert(0, attempts)
				use.insert(0, guess)
				return 'password is {}. found in {} guesses.'.format(guess, attempts)
				print(guess + str(attempts)		
			else:
				use.insert(0, guess)
				attempt_num.insert(0, attempts)


num = input("How many characters is max? : ")
correction = int(num) * "9"

guess_password(correction)


while True:
	command = input("Command -> ")
	commands = "find"
	print("commands are case sensitive!")
	print(commands)
	if command == "find":
		find_ = input("What is the arrangement of letters you would like to find? -> ")
		if find_ in use:
			i = 0
			for x in range(0, 9999999):
				if find_ == use[i]:
					attempt_numCurr = i
					break
			print(attempt_numCurr)
	if command == "use":
		find_ = input("What is the arrangement of letters you would like to use? -> ")
		if find_ in use:
			i = 0
			for x in range(0, 9999999):
				if find_ == use[i]:
					attempt_numCurr = i
					break
				print(attempt_numCurr)
