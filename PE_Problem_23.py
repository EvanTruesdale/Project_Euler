from math import sqrt, floor

def get_sum_of_divisors(input_n):
	# Start off with N/1, which will always work
	total = 1
	i = 2
	divisors_list = []
	while i <= floor(sqrt(input_n)):
		if input_n % i == 0:
			divisors_list.append(i)
			divisors_list.append(input_n / i)
		i += 1
	divisors_list = list(set(divisors_list))
	return sum(divisors_list)

abundant_n = 12
abundant_list = []
while abundant_n <= 28123:
	if abundant_n < get_sum_of_divisors(abundant_n):
		abundant_list.append(abundant_n)
	abundant_n += 1

total = 0
n = 1
lower_index = 0

def sum_of_abundants_value(input_n, input_lower_index):
	for i in range(len(abundant_list)):
		for j in range(i, len(abundant_list)):

			if abundant_list[i] + abundant_list[j] > input_n:
				break
			if abundant_list[i] + abundant_list[j] == input_n:
				#print("sum of: " + str(abundant_list[i]) + " " + str(abundant_list[j]))
				return 0
		if abundant_list[i] * 2 >= input_n:
			break
	return input_n

while n <= 28123:
	if n % 100 == 0:
		print(str(n))
	total += sum_of_abundants_value(n, lower_index)
	
	n += 1
print(total)