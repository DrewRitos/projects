import time
from time import sleep
import random
def abs(x):
	if x < 0:
		return -1*x
	else:
		return x
#I honestly don't know what's going on
k = 0 #Don't touch
time = 0 #Don't touch
timer = 20 #Self-explanatory
spaces = 20 #Other thing
length = 1 #Don't touch
length2 = 0 #Don't touch
flux = 1 #Don't touch
maxflux = 120 #Lower = faster, must be higher than 5 and lower than maxheight
startflux = 5 #Don't touch
incflux = 1 #Don't touch
char = " " #Character unit used
maxheight = 300 #Max amount of characters in a single line
midc = "{}"
space = "X"
fps = 40 #Self-explanatory
while True:
	sleep(1/fps)
	time += 1/fps
	if flux < maxflux and k == 0:
		flux += incflux
	elif flux <= 4:
		flux += incflux
		k = 0
	else:
		flux -= incflux
		k = 1
	length += length/flux
	slope = abs(length-length2)
	length2 = length
	mid = int(slope)
	if mid == 0:
			mid += 1
	if 2*length+spaces >= 0.9*maxheight:
		while True:
			sleep(1/fps)
			time += 1/fps
			if flux < maxflux and k == 0:
				flux += incflux
			elif flux <= 4:
				flux += incflux
				k = 0
			else:
				flux -= incflux
				k = 1
			length -= length/flux
			slope = abs(length-length2)
			length2 = length
			mid = int(slope)
			if mid == 0:
				mid += 1
			if length <= 0.1*maxheight:
				break
			print(char*int(length)+space*int(spaces/2-slope/2)+midc*mid+space*int(spaces/2-slope/2)+char*int(maxheight-(length+spaces)))
			if time >= timer:
				break
	print(char*int(length)+space*int(spaces/2-slope/2)+midc*mid+space*int(spaces/2-slope/2)+char*int(maxheight-(length+spaces)))
	if time >= timer:
		break
print(char*(int(2*length)+int(spaces)))
print(char*(int(2*length)+int(spaces)))
print(char*(int(2*length)+int(spaces)))
