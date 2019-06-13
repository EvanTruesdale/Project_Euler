from math import floor
n = 999
record = 0

def get_decimals(input_n):
	dividend = 10
	divisor = input_n
	decimal_str = ""
	i = 0
	pairs = []

	while True:
		i += 1

		#division
		quotient = floor(dividend / divisor)
		dividend = (dividend % divisor) * 10

        #repition detection
		decimal_str += str(quotient)
		pair = (quotient, dividend)
		if pair in pairs:
			return i - pairs.index(pair), input_n
		pairs.append(pair)

while True:
	if n < record:
		break

	repition, d = get_decimals(n)
	if repition > record:
		record = repition
	n -= 1

print(d)