import itertools
import string

use = []
attempt_num = []

use2 = open("use.txt", "w")

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
				return
				print(guess + str(attempts))	
			else:
				use.insert(0, guess)
				attempt_num.insert(0, attempts)


num = input("How many characters is max? : ")

if int(num) > 0 and int(num) < 1000:
	correction = int(num) * "9"

guess_password(correction)


while True:
	commands = "find, use"
	print("commands are case sensitive!")
	print(commands)
	command = input("Command -> ")
	if command == "find":
		find_ = input("What is the arrangement of letters you would like to find? -> ")
		if find_ in use:
			i = 0
			attempt_numCurr = i
			print("Find in use")
			while find_ != use[i]:
				i += 1
				if find_ == use[i]:
					attempt_numCurr = i
					print(attempt_numCurr)
	if command == "use":
		use_ = input("What is the arrangement of letters you would like to use? -> ")
		if use_ in use:
			print("Looking... please stand by!")
			i = 0
			for x in range(0, 999999):
				pass
			for x in range(0, len(use_)):
				if use_ == use[i]:
					attempt_numCurr = i
				else:
					i += 1
				print(str(attempt_numCurr))
			use2.write(use[attempt_numCurr])
	if command == "quit()" or command == "exit":
		quit()