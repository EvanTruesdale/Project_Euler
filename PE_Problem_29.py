sequence = []
for a in range(2, 101):
	for b in range(2, 101):
		sequence.append(a**b)
	print(a)

sequence = list(set(sequence))
print(len(sequence))