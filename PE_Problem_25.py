import math
import sys

f1 = 1
f2 = 1
n=3

def is_digitsLong(index, digits, f1_in, f2_in):
	f1 = f1_in
	f2 = f2_in
	for i in range(3, index+1):
		ftemp = f2
		f2 += f1
		f1 = ftemp

		if len(str(f2)) >= digits:
			return True, i
	return False, -1

while True:
	print(n)
	if is_digitsLong(n, 1000, f1, f2)[0]:
		print("Success - N: " + str(n))
		break
	n+=1