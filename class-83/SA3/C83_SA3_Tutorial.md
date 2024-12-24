Encrypt and Decrypt the Data
======================


In this activity, you will learn to decrypt the message using the private key value.


<img src= "https://s3-whjr-curriculum-uploads.whjr.online/501e9e1e-d9c9-4362-a46a-f972dd76d1dc.gif" width = "658" height = "324">




Follow the given steps to complete this activity.


* Open the file encrypt.py.


* Define a decrypt function that takes the ciphered text and the privateKey as parameters.


    `def decrypt(ciphertext, privateKey):`


* Get privateExponent and modulus from privateKey.


    ` privateExponent, modulus = privateKey`


* Perform calculations using the private key exponent and modulus value to decrypt the ciphered text and join the characters as a plain text.
 
  ` plaintext = ''.join([chr((char ** privateExponent) % modulus) for char in ciphertext])`


    ` return plaintext`


* Save the code to import the decrypt() function.
   


* Open the file app.py.
* Import the decrypt() function from the encrypt.py file. 

    `from encrypt import generateKeys, encrypt, decrypt`


* Type # to hide the decipher() functions of sender, receiver, and amount.  


    `  # sender = decipher(sender, 2)`
    
    ` # receiver = decipher(receiver, 2)`
    
    `  # amount = decipher(amount, 2) `


* Call the decrypt() function to decode the data inside the sender, receiver, and amount.  


    ` sender = decrypt(sender, privateKey)`
    
    ` receiver = decrypt(receiver, privateKey)  `
    
    ` amount = decrypt(amount, privateKey)`


* Save and run the code to check the output.
