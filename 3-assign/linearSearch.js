const bananaList = "bananas".split(""); // ["b", "a", "n", "a", "n", "a", "s"]
let globalArr = []
const linearSearch = (wordIdx, bananaList) => { //to search for the first letter
    return bananaList.indexOf(wordIdx)
}

console.log(linearSearch("a", bananaList)); // 1

const globalSearch = (wordIdx, bananaList) => { 
    for (let i = 0; i < bananaList.length; i++)
        if (bananaList[i] === wordIdx){ //if the index element is equal to the letter
            globalArr.push(i)
        }
        return globalArr
    // return bananaList.map((letter), i == 0 => letter[i]);
}


console.log(globalSearch("a", bananaList));
console.log(linearSearch("a", bananaList));