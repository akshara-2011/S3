import random
import math

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n/2 +1)):
        if n % i == 0:
            return False
    return True

''' 
   Modify the generate prime to take range of numbers to find a prime number in between.
   If no prime is found then return "Prime dose not exits in given range"
'''

# Take two numbers as parameters  x,y
def generatePrime():
    # Initialize prime to x
    prime = random.randint(2**10, 2**11)
    
    while not isPrime(prime):
        prime += 1      
        # Check if prime becomes greater then y and return "Prime dose not exits in given range"

    return prime

# Pass two numbers between which you want to find prime number(make sure first number is smaller)
num = generatePrime()
print("Prime number in given range:", num)

