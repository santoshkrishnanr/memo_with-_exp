
// memoize function to take a function as argument.
const memoize = (fn) => {
    const memory = new Map()

    return function(a,b,c){
        //unique address to store value (resolver)
        x = a.toString(16)+b.toString(16)+c.toString(16);

        // if there is some value in this unique address in memory 
        if(memory.has(x)){
            tem=memory.get(x)

            // to check if that value stored from last 5000 ms.
            if (Date.now()-(tem.Time) <= 5000){
                console.log('from memory ');
                return memory.get(x);
            }
        }

 // if not in memory run the function with given parameter
        const result = fn(a,b,c)
        //saving the output of function with timestamp TIME: and value:
        memory.set(x,{Time: Date.now(),value:result})
        return memory.get(x);
    };
};
    
// to have delay in milliseconds
function sleep(milliseconds) {
    var currentTime = new Date().getTime();
 
    while (currentTime + milliseconds >= new Date().getTime()) {
    }
 }


//function doing something and returning value in this case current date and time
const addToTime = (year, month,day ) => {
    console.log('i ran this function with arg  '+year,month, day  );
    // return data is stored as value: in this case (datenow+ datetime)
    return Date.now() + Date()
}



//const fastaddToTime = memoize(addToTime,(year, month, day) => year + month + day, 5000);
// in this case function and timeout is not sent as argument.
const fastaddToTime = memoize(addToTime);



// calling the function multiple times to show the usage of memory
// after 5000 ms the result is updated for same argument.
console.log(fastaddToTime(1,10,26));
console.log(fastaddToTime(1,10,26));
sleep(5000);
console.log(fastaddToTime(1,10,26));

