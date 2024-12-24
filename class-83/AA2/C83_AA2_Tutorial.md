Find the Prime Numbers for a Range 
===================


In this activity, you will modify the generatePrime() function to find the prime numbers within the input range.


<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/1525749/images/10644591/pasted-from-clipboard.png" width = "524" height = "244">



Follow the given steps to complete this activity.


* Open the file encrypt.py.


* Modify the generatePrime() function to pass two numbers, x and y, as parameters. 


     `def generatePrime(x, y):`


* Initialize the variable prime to x as the starting value of the range. 


    ` prime = x`
    	    
* Return the notification "Prime does not exist in the given range if the prime number cannot be found till the end of range value y."


    ` if prime > y:`
    
    `           return "Prime does not exist in the given range." `   


* Pass two numbers between which the prime number is to be found(make sure the first number is smaller).


    ` num = generatePrime(40, 200)`


* Save and run the code to check the output.
