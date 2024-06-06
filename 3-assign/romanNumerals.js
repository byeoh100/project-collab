const toRomanLazy = (num) => {
    let output = "";
    romanNumeralToArabic = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    };
    romanNumeralPriorityOrder = ["M", "D", "C", "L", "X", "V", "I"];
    for(let char of romanNumeralPriorityOrder) {
        let addChar = Math.floor(num / romanNumeralToArabic[char]);
        while(addChar > 0) {
            output += char;
            num -= romanNumeralToArabic[char];
            addChar -= 1
        }
    }
    console.log(output)
}

toRomanLazy(1556)