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

    for i in range(len(roman_numeral)):
        arabic_numeral = roman_numeral_to_arabic[roman_numeral[i]]
        times_div = int(num / arabic_numeral)

        while(times_div > 0):
            if times_div >= 4:
                if output[-1:] == roman_numeral[i - 1]:
                    output = output[-2::-1] + roman_numeral[i] + roman_numeral[i - 2]
                    num -= roman_numeral_to_arabic[roman_numeral[i]] * 9
                    times_div -= 4
                else:
                    output += roman_numeral[i] + roman_numeral[i - 1]
                    num -= roman_numeral_to_arabic[roman_numeral[i]] * 4
                    times_div -= 4
            if num <= 0:
                break
            output += roman_numeral[i]
            num -= arabic_numeral
            times_div -= 1

    return output

print(to_roman(1994))