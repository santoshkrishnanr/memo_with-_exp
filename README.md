# memo_with-_exp
a test project. 

#Description :
memo_with_exp "memoize with expiration"

 * To Creates a function that memoizes the result of func. If resolver is provided,
 * it determines the cache key for storing the result based on the arguments provided to the memorized function.
 * By default, the first argument provided to the memorized function is used as the map cache key. The memorized values
 * timeout after the timeout exceeds. The timeout is in defined in milliseconds.
 
##Summary
 In Nutshell!! a program function when called gives some output result. But when called again with same arguments should return the value from the memory instead of running the the function agian. hence saving execution time of function.
 
 The value stored (of a particular parameters)can only be used for a particular time. Later when called should be updated by running the given function again. 
 
 
##Strategy and Implementation:

 *By sending a the time(ms) with the parameters the return value from the function can be stored with an expiry-timestamp
    
   * Advantage over saving with current timestamp => Each result can have different expiry-time 
 
 *By sending a function as parameter this can be implemented and upgraded work with different function.
 
 *The executed values of function can be stored in 
   * In memory 
   * In Text file
   * In server. 
 - With its own advantages like sharing values between programs or different users etc.
   for simplicity it is just stored in memory as a dictionary/map.
   
 *Deleting the values after expiration time can also be implemented to save storage space making volatile result.-auto delete function
   
 *Resolver has to save the value with its unique parameter. As each parameter sent to a function gives a unique result and it has to be saved with unique address
   * for Example :-address=(year+month+day)
       - for (1+11+1)=(0+1+12) both address are same 13 but output result from function are different.
   
   * To solve this each parameter is converted to -hex value and used as address
      - address= (hex(year)+hex(month)+hex(day))
      - when (1+11+1)!=(0+1+12)
  
  
#Memoization using node.js

The above described program is written in JavaScript [memoization_.js](https://github.com/santoshkrishnanr/memo_with-_exp/blob/main/memoizaton_.js)
and can be checked using node.js 

##Requirements
For development, you will need Node.js and a node global package, npm installed in your environment. Or use [install](https://nodejs.org/en/download/)
which includes node.js and npm.
* Download:[memoization_.js](https://github.com/santoshkrishnanr/memo_with-_exp/blob/main/memoizaton_.js) and [package.json]()for dependencies using $npm install.

##Run the project

Go to the file location from terminal and run
```
* $node memoizaton_.js
```
It can be seen that the value printed will change when it is called after the timeout.
 
 