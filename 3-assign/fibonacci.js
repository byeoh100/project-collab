
function fibonacci(num){

    if (num === 0){
        return num
    }
    else if (num === 1){
        return num
    }
    num1 = 0
    num2 = 1

    for (let idx = 0; idx < num-1; idx++){
        sum = (num1) + (num2)
        num1 = num2
        num2 = sum
    }
    console.log(sum)
}

fibonacci(3)