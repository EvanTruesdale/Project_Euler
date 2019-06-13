n = 2
sum_of_powers = []

while True:
	total = 0
	#print(n)
	for i, digit in enumerate(str(n)):
		total += int(digit) ** 5
	if total == n:
		sum_of_powers.append(n)
		print("TRUE")
		print(sum(sum_of_powers))
	n += 1