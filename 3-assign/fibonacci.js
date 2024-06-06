const fibonacci = (num) => {
    if(num === 0) {
        return 0;
    }
    else if(num === 1) {
        return 1;
    }
    let currVal = 1;
    let preVal = 0;
    num -= 1;
    while(num > 0) {
        let temp = currVal;
        currVal += preVal;
        preVal = temp;
        num -= 1
    }
    return currVal;
}

console.log(fibonacci(7))