function factorialFunc(num){
    if (num === 1){ //if number that is being passed in the argument is 1...
        return num 
    }
        return num * factorialFunc(num-1) //calls back itself, and returns num-1 in the argument function until it hits the base case
}

console.log(factorialFunc(3))