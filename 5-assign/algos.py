def armstrong():                                # Returns armstrong numbers up to 999
    n = 0
    is_armstrong = []
    while n < 1000:
        compare = 0
        n_list = list(str(n))
        digits = len(n_list)
        for i in n_list:
            compare += pow(int(i), digits)
        if compare == n:
            is_armstrong.append(n)
        n += 1
    return is_armstrong

def is_anagram(str1, str2):                     # Returns if str1 is an anagram of str2
    if len(str1) != len(str2):
        return False
    str1 = str1.lower()
    str2 = str2.lower()
    str2_list = [x for x in str2]
    for i in str1:
        if i in str2_list:
            str2_list.remove(i)
    if not str2_list:
        return True
    else:
        return False

def anagrams_for(str, word_list):               # Return list of words that are an anagram of given str from word_list
    ret_list = []
    for i in word_list:
        if is_anagram(str, i) == True:
            ret_list.append(i)
    return ret_list

def sum_pairs(num_list, sum):                   # Finds pair of numbers that add to desired sum from num_list
    ret_list = []
    for i in num_list:
        if sum - i in num_list:
            ret_list.append([i, sum - i])
            num_list.remove(sum - i)
    return ret_list

def credit_check(num):                          # Checks given num (as a str) as valid number based on Luhn's algo
    num_len = len(num)
    even_or_odd = num_len % 2
    num_list = []
    
    for i in range(num_len):
        append_num = int(num[i])
        if append_num * 2 > 9 and i % 2 == even_or_odd:
            append_num = (append_num * 2) % 10 + 1
            num_list.append(append_num)
        elif i % 2 == even_or_odd:
            num_list.append(append_num * 2)
        else:
            num_list.append(append_num)

    return sum(num_list) % 10 == 0

def char_count(str):                            # Takes string and returns list of lists of letter frequency in descending order
    sorted_str_list = sorted([x for x in str])
    char_dict = {}
    count_list = []
    for i in sorted_str_list:
        if i == " ":
            continue
        if i not in char_dict:
            char_dict[i] = 1
        else:
            char_dict[i] += 1
    
    for key, value in char_dict.items():
        count_list.append([key, value])

    count_list.sort(key=lambda x : x[1], reverse = True)
    return count_list

def palindrome(word):                           # Checks if word is palindome, need to complete challenge
    if type(word) != str:
        word = str(word)

    end = len(word) - 1

    for start in range(len(word)):
        if start >= end:
            return True
        if word[start] != word[end]:
            return False
        end -= 1
        
def calculate_mode(lst):
    freq_dict = {}
    for i in lst:
        if i not in freq_dict:
            freq_dict[i] = 1
        else:
            freq_dict[i] += 1
    freq_dict = sorted(freq_dict.items(), key=lambda kv: kv[1], reverse = True)

    ret = []
    max = 0
    for key, value in freq_dict:
        if value >= max:
            max = value
            ret.append(key)
    return ret

def pad(lst, size, insert = None):
    if len(lst) >= size:
        return lst
    else:
        while(len(lst) < size):
            lst.append(insert)
    return lst

def isValid(s: str) -> bool:
    brac_list = {
        ")" : "(",
        "]" : "[",
        "}" : "{"
    }
    brac_stack = []
    brac_open = 0
    brac_close = 0
    valid_open_bracket = brac_list.values()
    for i in s:
        brac_stack.append(i)
        if i in valid_open_bracket:
            brac_open += 1
        else:
            brac_close += 1
            if brac_close > brac_open:
                return False
            if brac_list[i] == brac_stack[-2]:
                brac_stack.pop()
                brac_stack.pop()
                brac_close -= 1
                brac_open -= 1
    if not brac_stack:
        return True
    else:
        return False
    
print(isValid("(){}}{"))