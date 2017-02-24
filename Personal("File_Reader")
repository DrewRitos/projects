def print_file(x):
	b = ""
	for line in x:
		b += line
	return b
while True:
	try:
		direct = input("Input file directory:")
		_file_multiuse = open(direct,"r+")
	except OSError:
		print("\nFile directory not found! Try again.\n")
	except:
		print("\nAn error has been raised, but was caught by my incredible exception handling skills. Please try again.\n")
	else:
		break

print(print_file(_file_multiuse))
