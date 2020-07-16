import math
import sys

def is_abundant(num):
    n = 2
    divisors = [1]
    while n <= math.sqrt(num):
        if num % n == 0:
            divisors.append(n)
            divisors.append(num/n)
        n += 1
    divisors = list(set(divisors))
    if sum(divisors) > num:
        return True
    return False

abundant_nums = []
n = 1
while n <= 28124:
    if is_abundant(n):
        abundant_nums.append(n)
    n += 1

def sum_test(num):
    i_1 = 0
    i_2 = 0
    max_i = len(abundant_nums)
    abundant_1 = abundant_nums[i_1]
    abundant_2 = abundant_nums[i_2]
    sum = abundant_1 + abundant_2
    while abundant_1 <= num and i_1 < max_i-1:
        while sum <= num:
            sum = abundant_1 + abundant_2
            if sum == num:
                return True
            i_2 += 1
            abundant_2 = abundant_nums[i_2]
        i_1 += 1
        i_2 = i_1
        abundant_1 = abundant_nums[i_1]
        abundant_2 = abundant_nums[i_2]
    return False

sum = 0
n = 1
limit = 28123
while n <= limit:
    sys.stdout.write("\r" + str(int(100*n/limit)) + "%")
    if sum_test(n) == False:
        sum += n
    n += 1
print("")
print(sum)
