Validate the Data Received
======================


In this activity, you will learn to validate the hash data received.


<img src= "https://s3-whjr-curriculum-uploads.whjr.online/1e5652a0-6c8d-4561-bd87-6f9b594bda43.gif" width = "180" height = "320">




Follow the given steps to complete this activity:


* Open the file app.py.


* Check a condition for getting an argument request from form 1 as f1.


    ` elif request.args.get("form") == "f1":`


* Fetch and store the sender, receiver, amount, and hash data from the form
	` else 
sender = request.form.get("sender")
        	receiver = request.form.get("receiver")
        	amount = request.form.get("amount")
        	hash = request.form.get("hash")`


* Using concatenation, pass the form data as a single argument to the generateHash() function to generate a validation hash. Store the new hash as validationHash.
`validationHash = generateHash(sender+receiver+amount)`


*What will you change in the code to display the correct notification?
The notifications within the if and the else blocks will need to be swapped.
`if validationHash == hash:
  message= "Success"  
else:
       message = "Failed"  `


* Create a “validation” dictionary and store “message”, “blockHash”, and “validationHash” keys in it with their respective values.


`  validation = { 
               "message": message,
               "blockHash": hash,
               "validationHash": validationHash 
        }  
`


* Save and run the code to check the output.
