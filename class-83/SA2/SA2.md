Generate a Hash Value Using an Algorithm
===================


In this activity, you will learn about the secure hashing algorithm (SHA)and use it to encrypt the block data.




<img src= "https://s3-whjr-curriculum-uploads.whjr.online/71a69a96-7e32-4bf0-baa3-54ba61bc05b5.gif" width = "180" height = "320">




Follow the given steps to complete this activity.


* Open the file hash.py.


* Import the hashlib library to use the hashing techniques.


     `import hashlib`   


* Create a hash object by using SHA sha256().
`hash_object = hashlib.sha256()`


* Update the hash object to accept the input string.


    	` hash_object.update(input_string.encode('utf-8'))`


* Generate the hash value for the input string using the hexdigest() method.


    	` hash_value = hash_object.hexdigest()`


* Save and run the code to check the output.
