import time
from time import sleep
length = 1 #Don't touch
flux = 0 #Don't touch
maxflux = 20 #Slope
incflux = 1 #Don't touch
char = "-" #Character unit used
maxheight = 25 #Max amount of characters in a single line
while True:
	sleep(1/60)
	if flux < maxflux:
		flux += incflux
	else:
		flux -= incflux
	length += length/flux
	if length > maxheight:
		while True:
			sleep(1/60)
			if flux < maxflux:
				flux += incflux
			else:
				flux -= incflux
			length -= length/flux
			if length < 4:
				break
			print(char*int(length))
	print(char*int(length))
