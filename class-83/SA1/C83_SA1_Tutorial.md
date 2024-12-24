Generate Keys as Prime Numbers
===================


In this activity, you will learn to generate the keys as prime numbers.


<img src= "https://s3-whjr-curriculum-uploads.whjr.online/b0a7910e-0fc7-456c-8fb8-af9e269ca36c.png" width = "725" height = "415">


Follow the given steps to complete this activity.


* Open the file encrypt.py.


* Define a generatePrime() function to generate a random number and check if it’s a prime number.


    ` def generatePrime():`


* Generate a random number between a specified range. 
(Use a larger number using a higher range for more security. Example: Between 2**8 and 2**9)


    ` prime = random.randint(2**8, 2**9)`


* Check if the random number generated is a prime number using the user defined function isPrime(), or find the next number by incrementing the number until a prime number is found.


    `    while not isPrime(prime):`      
    ` prime += 1`  
    ` return prime`


* Find 2 random prime numbers and print them by defining a generateKeys() function.

	` def generateKeys():`

    ` prime1 = generatePrime() `

	` prime2 = generatePrime() `
    
    ` print(prime1, prime2)`


* Call the generateKeys() function to generate two prime numbers.


	` generateKeys()`

* Save and run the code to check the output.
