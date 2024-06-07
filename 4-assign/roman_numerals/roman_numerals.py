def to_roman(num):
    output = ""
    roman_numeral_to_arabic = {
        "M" : 1000,
        "D" : 500,
        "C" : 100,
        "L" : 50,
        "X" : 10,
        "V" : 5,
        "I" : 1
    }

    roman_numeral = ["M", "D", "C", "L", "X", "V", "I"]

    for i in roman_numeral:
        arabic_numeral = roman_numeral_to_arabic[i]
        times_div = int(num / arabic_numeral)
        while(times_div > 0):
            output += i
            num -= arabic_numeral
            times_div -= 1
    return output