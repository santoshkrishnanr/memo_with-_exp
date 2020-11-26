# memo_with-_exp
a test project. 

## Description :
memo_with_exp "memoize with expiration"

 * To Creates a function that memoizes the result of func. If resolver is provided,
 * it determines the cache key for storing the result based on the arguments provided to the memorized function.
 * By default, the first argument provided to the memorized function is used as the map cache key. The memorized values
 * timeout after the timeout exceeds. The timeout is in defined in milliseconds.
 
## Summary
 In Nutshell!! a program function when called gives some output result. But when called again with same arguments should return the value from the memory instead of running the the function agian. hence saving execution time of function.
 
 The value stored (of a particular parameters)can only be used for a particular time. Later when called should be updated by running the given function again. 
 
 
### Strategy and Implementation:

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


## Memoization using Python
The above described program is written in Python [memoization.py](https://github.com/santoshkrishnanr/memo_with-_exp/blob/main/memoization.py)
and can be tested using pytest [test_memo.py](https://github.com/santoshkrishnanr/memo_with-_exp/blob/main/test_memo.py)  

### Requirements
For development, you will need Python3 and pytest installed on your environment. Or use [Python](https://www.python.org/downloads/) and [Pytest](https://docs.pytest.org/en/stable/getting-started.html).
 * Download:[memoization.py](https://github.com/santoshkrishnanr/memo_with-_exp/blob/main/memoization.py)
 & [test_memo.py](https://github.com/santoshkrishnanr/memo_with-_exp/blob/main/test_memo.py) 
 
### To Run the Project 
Go to the file location from terminal and run
````
$python memization.py
````
To check manually 
````
    print(memoize(add_to_time, y, m, d, timeout))
    print(memoize(add_to_time, y, m, d, timeout))
    time.sleep(timeinsec)
    print(memoize(add_to_time, y, m, d, timeout))
````
To test manually 
 * Timeout store the amount of time (in ms) the value has to be stored of a function name (add_to_time) with parameter(y,m,d)
 * For Example: 
 ````
    print(memoize(add_to_time, 1, 5, 4, 5000))
    print(memoize(add_to_time, 1, 5, 4, 5000))
    time.sleep(5)
    print(memoize(add_to_time, 1, 5, 4, 5000))
````   
 * It can be seen that when the function is called for the first time the value is displayed and stored 
 * later when called it it gives the same value(from memory) until the  given timeout time 
 * later when called after the initial timeout time the value is updated, stored and displayed.   
 
 
### Testing the program 
To test the program [memoization.py](https://github.com/santoshkrishnanr/memo_with-_exp/blob/main/memoization.py) using pytest.
Simply run $pytest after going the file location from terminal.or $pytest<filename.py> -v -s to check each test condition with its printed output.

## Testing conditions:
* To check the uniqueness of resolver address.\
      test_resolver(): Is used 
     * It checks for all the combinations of three variables (y,m,d) each having  the range of values from (0 to 11)
     * result are stored and check for repetition.

* To check the value from function and value from memory are same.\
      test_memoize(): Is used 
     * It checks the output value by calling twice.
        
* To check for the time required to return values after executing  the function and to  return from memory.\
    def test_run_time():
     * Just calculates the time before and after runing a function twice .
         
* To check for the amount of time value is stored in memory for use\
    def test_cached_time():
    * Calls a function and checks if the function is same for the same parameter until its updated
    *Gives the time of storing the value.

* To check for the amount of time previous value is stored in memory\
    def test_updated_value():
    * Calls a function and checks if the function is greater for the same parameter until its updated
    *Gives the time of updating the value.

* To check for clock tamper /fake clock(by incrementing time ) \
    def test_time_clock():
    * Calls a function and checks if the function is greater for the same parameter until its updated
    *Gives the time of updating the value.


* each test can also be run individually by pytest <filename.py>::<test_fun()> \



## Memoization using node.js

The above described program is written in JavaScript [memoization_.js](https://github.com/santoshkrishnanr/memo_with-_exp/blob/main/memoizaton_.js)
and can be checked using node.js 

### Requirements
For development, you will need Node.js and a node global package, npm installed in your environment. Or use [install](https://nodejs.org/en/download/)
which includes node.js and npm.
* Download:[memoization_.js](https://github.com/santoshkrishnanr/memo_with-_exp/blob/main/memoizaton_.js) and [package.json]()for dependencies using $npm install.

### Run the project

Go to the file location from terminal and run
```
* $node memoizaton_.js
```
It can be seen that the value printed will change when it is called after the timeout.
````
console.log(fastaddToTime(1,10,26));
sleep(4000);
console.log(fastaddToTime(1,10,26));
````
 by changing the sleep("value"); and calling it again the change in value can be observed.
 
### Additional implementations:
* Data can be stored in a txtfile or database.
* To save the memory space auto deletion of data function.
* Implementation of timeout for different values and function call
     