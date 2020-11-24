const memoize = (fn) => {
    const memory = new Map()

    return function(a,b,c){
        //unique address to store value (resolver)
        x=a+b+c;

        // if there is some value in this unique address in memory 
        if(memory.has(x)){
            tem=memory.get(x)
            // if that value stored from last 5000 ms.
            if (Date.now()-(tem.Time) <= 5000){
                console.log('from memory ');
                return memory.get(x);
            }
        }

 // if not in memory run the function with given agrgument 
        const result = fn(a,b,c)
        //saving the output of function with timestamp TIME: and value:
        memory.set(x,{Time: Date.now(),value:result})
        return memory.get(x);
    };
};
    
// to have delay 
function sleep(miliseconds) {
    var currentTime = new Date().getTime();
 
    while (currentTime + miliseconds >= new Date().getTime()) {
    }
 }

//function doing something and returning value in this case current date and time  

const addToTime = (year, month,day ) => {

    console.log('i ran this function with arg  '+year,month, day  );
    // return data is stored as value: in this case  
    return Date.now() + Date()
}

//const fastaddToTime = memoize(addToTime,(year, month, day) => year + month + day, 5000);
const fastaddToTime = memoize(addToTime);



console.log(fastaddToTime(1,11,26));
console.log(fastaddToTime(1,11,6));
sleep(5000);
console.log(fastaddToTime(1,11,26));

