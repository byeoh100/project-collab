
function fibonacci(num){ //we are using num for iterating thru a created sequence, not using it as an element

    arr = []

    if (num === 0){ //we already know that if the number = 1 starting in the fibonacci sequence, will equal to 1
        return num
    }
    else if (num === 1){ //we already know that if the number = 1 starting in the fibonacci sequence, will equal to 1
        return num
    } 
    num1 = 0 
    num2 = 1

    for (let idx = 0; idx < num-1; idx++){ //we will be iterating through, we do num-1 to ensure i want to iterate specfically num times
        sum = (num1) + (num2)
        num1 = num2 //makes the num equal the next num of the fib sequence
        num2 = sum //makes the num equal the sum, because it will the next num of the fib sequence after num1
        arr.push(sum); 


    }
    console.log(arr)
}

fibonacci(3)