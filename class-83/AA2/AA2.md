Generate hash value of fixed length
===================


In this activity, you will have to generate a hash value of fixed length with the help of a fixed prime number.


<img src= "https://s3-whjr-curriculum-uploads.whjr.online/a83803b7-537a-4aed-926c-278c7d1ce2da.png" width = "180" height = "320">




Follow the given steps to complete this activity.


* Open the file hash.py.


* Create variables to store a prime number and a hash length of your choice.  


     ` prime = 31
   	 hashLength = 8 `


* Calculate the hash value using the equation “(hashValue * prime + ord(char))”. You can write your own equation too!


     		`hashValue = (hashValue * prime + ord(char))`
    	    
* Use the mod operator to reduce the hash to the fixed length.


    	`hashValue = hashValue % 10 **  hashLength`   


* Convert the hash value to a fixed-length string by padding with zeros if necessary.


     		`hashValue = str(hashValue).zfill(hashLength)`


* Save and run the code to check the output.
