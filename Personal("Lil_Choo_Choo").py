import time
lay1 = "o o o o o o O O"
lay2 = ",_____  ____    O"
lay3 = "| PMD \_|[]|_'__Y"
lay4 = "|_______|__|_|__|}"
bot = "booo--oo==oo--OOO\\\\"
trainformat = format(bot, "_<80s")
b = ""
k = 0
while True:
	time.sleep(0.05)
	k += 1
	if k > 61:
		break
	trainformat = trainformat[:-1]
	trainformat = "_"+trainformat
	if k%2 == 0 and k < 30:
		b = "o"
	else:
		b = " "
	lay1 = b+lay1
	lay2 = " "+lay2
	lay3 = " "+lay3
	lay4 = " "+lay4
	print("\n"*50)
	print(lay1+"\n"+lay2+'\n'+lay3+'\n'+lay4)
	print(trainformat)
