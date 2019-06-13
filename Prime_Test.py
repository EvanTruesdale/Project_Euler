import os
import math

def isPrime(input):
    if(input == 1):
        return False
    elif(input == 2):
        return True
    elif(input % 2 == 0):
        return False
    elif(input == 3):
        return True
    elif(input < 9):
        return True
    elif(input % 3 == 0):
        return False

    n = 5
    limit = math.ceil(math.sqrt(input))
    while True:
        if(input % n == 0):
            return False
        elif(input % (n + 2) == 0):
            return False
        if(n >= limit):
            return True
        n += 6

if __name__ == "__main__":
   test = input("Input: ")
   print(isPrime(test))
