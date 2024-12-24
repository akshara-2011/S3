import random

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n/2 +1)):
        if n % i == 0:
            return False
    return True

# Define generatePrime() function
def generatePrime():
    # generate a random number between 2**8 and 2**9 (can generate larger number if required of more security)
    prime = random.randint(2**8, 2**9)
    # Loop untill 'prime' variable doe not contain a prime number, check this with isPrime() function
    while not isPrime(prime):
        # Increment the 'prime' variable by 1
        prime += 1
    # return the 'prime' variable    
    return prime

# Define generateKeys() function
def generateKeys():
    # Use generatePrime() function to generate two numbers and stire them in prime1 and prime2
    prime1 = generatePrime() 
    prime2 = generatePrime()
    
    # Print the generated prime numbers
    print(prime1, prime2)

# Call the generateKeys() function to show the output
generateKeys()
