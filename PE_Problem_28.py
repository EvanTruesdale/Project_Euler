n = 1
d = 2
total = 0

while n < 1002001:
	for x in range(4):
		total += n
		n += d
	d += 2
total += n

print(total)