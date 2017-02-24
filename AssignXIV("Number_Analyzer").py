#_continue is the variable that determines if any while function continues or not
_continue = "yes"
#default is the callname I put in to any function that requires a parameter for what it will respond with if the 
#user inputs something that gets caught by exception handling
#get and getint are input functions that do exception handling 
default = "I'm sorry, I didn't get that. Please try again."
def getint(x,u="I'm sorry, I didn't get that. Please try again.",y="",z=""):
	while True:
		try:
			b = int(input(x))
		except:
			print("I'm sorry, I didn't get that. Please try again.")
		else:
			if y != "k":
				if y <= b <= z:
					return b
				else:
					print(u)
			else:
				return b
def get(x,u="I'm sorry, I didn't get that. Please try again.",y=0,z=0,c=0):
	while True:
		try:
			b = input(x)
		except:
			print("I'm sorry, I didn't get that. Please try again.")
		else:
			if y != 0:
				if b == y or z or c:
					return b
				else:
					print(u)
			else:
				return b
#is_even returns true if x is even and false if it isn't
def is_even(x):
	return bool(x % 2 == 0)
#is_square returns true if x is a perfect square and false if it isn't
def is_square(x):
	return bool(x**(1/2) == int(x**(1/2)))
#is_prime returns true if x is a prime number and false if it isn't
def is_prime(x):
	for p in range(2,x):
		if x%p == 0:
			return False
	return True
#Runs number analyzer menu code
print("Welcome to the Number Analyzer Code!\nYou can choose to:\n(1) analyze a single integer\n(2) examine a range of numbers\n(3) exit the program")
q1 = getint("Which would you like to choose?",default,1,3)
if q1 == 1:
	print("\nOkay, let's analyze a number.")
	while _continue == "yes":
		num = getint("\nEnter a number (1 - 100,000):",default,1,100000)
		if is_even(num):
			print(num,"is an even number.")
		else:
			print(num,"is an odd number.")
		if is_square(num):
			print(num,"is a perfect square.")
		else:
			print(num,"is not a perfect square.")
		if is_prime(num):
			print(num,"is a prime number.")
		else:
			print(num,"is not a prime number.")
		_continue = get("\nWould you like to analyze another number?",default,"yes","no")
if q1 == 2:
	print("\nOkay, great! Let's take a look at a range of range of numbers.")
	while _continue == "yes":
		lo = getint("\nEnter the lower number:",default,1,100000)
		hi = getint("Enter the higher number:",default,lo,100000)
		for t in range(lo,hi+1):
			if is_prime(t):
				print(t,"is a prime number.")
			else:
				pass
		_continue = get("\nWould you like to analyze another number?",default,"yes","no")
if q1 == 3:
	print("\nOkay, goodbye.")














