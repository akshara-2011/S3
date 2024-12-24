Generate the Public and Private Keys
===================


In this activity, you will learn to find the GCD and extended GCD to find the public and private exponent values.




<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/1525749/images/10638105/pasted-from-clipboard.png" width = "393" height = "92">


* Open the file encrypt.py.


* Loop until gcd() of publicExponent and coprimeCount is not equal to 1.


     `while gcd(publicExponent, coprimeCount) != 1:`
    
    ` publicExponent += 1`   


* Call the extendedGCD() function with publicExponent and coprimeCount and store the result in the “privateExponent” variable.


    `privateExponent = extendedGCD(publicExponent, coprimeCount)`

    ` privateExponent = privateExponent % coprimeCount`   


* Return both the public and private keys, the public key as the publicExponent with modulus, and the private key as the privateExponent  with modulus. 


    ` return (publicExponent, modulus), (privateExponent, modulus)`
 
* Get publicKey and privateKey from generateKeys() function and print their values.


    ` publicKey, privateKey = generateKeys()` 
    
    ` print(publicKey, privateKey)` 
*  Save and run the code to check the output.
