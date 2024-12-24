import random
import math
''' 
    The isPrime() function take a number 'n' and then starting from number 2 upto number n-1
    it will see if 'n' is divisible by any number. If yes then it returns False as number is not prime

    If not the it returns True

    See what is wrong in the function as 17 is prime but function is returning False for it.

'''
def isPrime(n):
    # Check if True and Flase returned correctly
    if n <= 1:
        return False
    # Check if range is give correctly
    for i in range(1, n):
        if n % i == 0:
            return False
    return False

# Also try for different number
num =17
result = isPrime(num)
print("Is ", num, "prime:", result)