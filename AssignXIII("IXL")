import random
#I import random to generate all of the numbers within each problem
print("Welcome to IXL")
#Asks the user what they want to practice for the first time
op = input("What skill would you like to practice today?")
#Starts a loop that allows the user to take multiple tests multiple times
while True:
	#The points are generated per user input, and num is equal to the question number the user is on
	points = 0
	num = 0
	#Determines which operator the user wants and randomly generates problems and asks the user them
	#If they reach 10 points, they win
	#If they get to -5 points, they lose
	#If they get a question right, they get 3 points
	#When they get it wrong, they lose 5 points
	if op == "+":
		while True:
			num += 1
			integer1 = random.randint(1,100)
			integer2 = random.randint(1,100)
			answer = integer1 + integer2
			q = float(input("\n"+str(num)+". "+str(integer1)+" + "+str(integer2)+" ="))
			if q == answer:
				print("Correct!")
				points += 3
				print("Points:",points)
			else:
				print("Incorrect. Try again")
				points -= 5
				print("Points:",points)
				while True:
					q = float(input("\n"+str(num)+". "+str(integer1)+" + "+str(integer2)+" ="))
					if q == answer:
						print("Correct!")
						points += 3
						print("Points:",points)
						break
					else:
						print("Incorrect. Try again")
						points -= 1
						print("Points:",points)
			if points >= 10:
				print("\nYou have mastered the skill of addition!")
				print("It took you",num,"questions to master this skill.")
				break
			elif points <= -5:
				print("Sorry, you dropped below the lowest possible score.\nYou may need some addition practice.\nGoodbye.")
				break
	elif op == "-":
		while True:
			num += 1
			integer1 = random.randint(51,100)
			integer2 = random.randint(1,50)
			answer = integer1 - integer2
			q = float(input("\n"+str(num)+". "+str(integer1)+" - "+str(integer2)+" ="))
			if q == answer:
				print("Correct!")
				points += 3
				print("Points:",points)
			else:
				print("Incorrect. Try again")
				points -= 5
				print("Points:",points)
				while True:
					q = float(input("\n"+str(num)+". "+str(integer1)+" - "+str(integer2)+" ="))
					if q == answer:
						print("Correct!")
						points += 3
						print("Points:",points)
						break
					else:
						print("Incorrect. Try again")
						points -= 1
						print("Points:",points)
			if points >= 10:
				print("\nYou have mastered the skill of subtraction!")
				print("It took you",num,"questions to master this skill.")
				break
			elif points <= -5:
				print("Sorry, you dropped below the lowest possible score.\nYou may need some addition practice.\nGoodbye.")
				break
	elif op == "//":
		while True:
			num += 1
			integer1 = random.randint(1,100)
			integer2 = random.randint(1,10)
			answer = integer1 // integer2
			q = float(input("\n"+str(num)+". "+str(integer1)+" // "+str(integer2)+" ="))
			if q == answer:
				print("Correct!")
				points += 3
				print("Points:",points)
			else:
				print("Incorrect. Try again")
				points -= 5
				print("Points:",points)
				while True:
					q = float(input("\n"+str(num)+". "+str(integer1)+" // "+str(integer2)+" ="))
					if q == answer:
						print("Correct!")
						points += 3
						print("Points:",points)
						break
					else:
						print("Incorrect. Try again")
						points -= 1
						print("Points:",points)
			if points >= 10:
				print("\nYou have mastered the skill of integer division!")
				print("It took you",num,"questions to master this skill.")
				break
			elif points <= -5:
				print("Sorry, you dropped below the lowest possible score.\nYou may need some addition practice.\nGoodbye.")
				break
	elif op == "*":
		while True:
			num += 1
			integer1 = random.randint(1,20)
			integer2 = random.randint(1,20)
			answer = integer1 * integer2
			q = float(input("\n"+str(num)+". "+str(integer1)+" * "+str(integer2)+" ="))
			if q == answer:
				print("Correct!")
				points += 3
				print("Points:",points)
			else:
				print("Incorrect. Try again")
				points -= 5
				print("Points:",points)
				while True:
					q = float(input("\n"+str(num)+". "+str(integer1)+" * "+str(integer2)+" ="))
					if q == answer:
						print("Correct!")
						points += 3
						print("Points:",points)
						break
					else:
						print("Incorrect. Try again")
						points -= 1
						print("Points:",points)
			if points >= 10:
				print("\nYou have mastered the skill of multiplication!!")
				print("It took you",num,"questions to master this skill.")
				break
			elif points <= -5:
				print("Sorry, you dropped below the lowest possible score.\nYou may need some addition practice.\nGoodbye.")
				break
	elif op == "random":
		p = random.randint(1,4)
		if p == 1:
			op = "+"
		elif p == 2:
			op = "-"
		elif p == 3:
			op = "//"
		elif p == 4:
			op = "*"
		if op == "+":
			num += 1
			integer1 = random.randint(1,100)
			integer2 = random.randint(1,100)
			answer = integer1 + integer2
			q = float(input("\n"+str(num)+". "+str(integer1)+" + "+str(integer2)+" ="))
			if q == answer:
				print("Correct!")
				points += 3
				print("Points:",points)
			else:
				print("Incorrect. Try again")
				points -= 5
				print("Points:",points)
				while True:
					q = float(input("\n"+str(num)+". "+str(integer1)+" + "+str(integer2)+" ="))
					if q == answer:
						print("Correct!")
						points += 3
						print("Points:",points)
						break
					else:
						print("Incorrect. Try again")
						points -= 1
						print("Points:",points)
		elif op == "-":
			num += 1
			integer1 = random.randint(51,100)
			integer2 = random.randint(1,50)
			answer = integer1 - integer2
			q = float(input("\n"+str(num)+". "+str(integer1)+" - "+str(integer2)+" ="))
			if q == answer:
				print("Correct!")
				points += 3
				print("Points:",points)
			else:
				print("Incorrect. Try again")
				points -= 5
				print("Points:",points)
				while True:
					q = float(input("\n"+str(num)+". "+str(integer1)+" - "+str(integer2)+" ="))
					if q == answer:
						print("Correct!")
						points += 3
						print("Points:",points)
						break
					else:
						print("Incorrect. Try again")
						points -= 1
						print("Points:",points)
		elif op == "//":
			num += 1
			integer1 = random.randint(1,100)
			integer2 = random.randint(1,10)
			answer = integer1 // integer2
			q = float(input("\n"+str(num)+". "+str(integer1)+" // "+str(integer2)+" ="))
			if q == answer:
				print("Correct!")
				points += 3
				print("Points:",points)
			else:
				print("Incorrect. Try again")
				points -= 5
				print("Points:",points)
				while True:
					q = float(input("\n"+str(num)+". "+str(integer1)+" // "+str(integer2)+" ="))
					if q == answer:
						print("Correct!")
						points += 3
						print("Points:",points)
						break
					else:
						print("Incorrect. Try again")
						points -= 1
						print("Points:",points)
		elif op == "*":
			num += 1
			integer1 = random.randint(1,20)
			integer2 = random.randint(1,20)
			answer = integer1 * integer2
			q = float(input("\n"+str(num)+". "+str(integer1)+" * "+str(integer2)+" ="))
			if q == answer:
				print("Correct!")
				points += 3
				print("Points:",points)
			else:
				print("Incorrect. Try again")
				points -= 5
				print("Points:",points)
				while True:
					q = float(input("\n"+str(num)+". "+str(integer1)+" * "+str(integer2)+" ="))
					if q == answer:
						print("Correct!")
						points += 3
						print("Points:",points)
						break
					else:
						print("Incorrect. Try again")
						points -= 1
						print("Points:",points)
		if points >= 10:
				print("\nWow, you are a master of mathematics! Congratulations on your achievement.")
				print("It took you",num,"questions to master this skill.")
				break
		elif points <= -5:
			print("Sorry, you dropped below the lowest possible score.\nYou may need some addition practice.\nGoodbye.")
			break

	op = input("\nWould you like to try another skill?")
	if op == "no":
		break
