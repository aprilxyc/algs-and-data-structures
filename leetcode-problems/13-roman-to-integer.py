# roman integers
# this problem was okay. Initially thought of using a stack but wrong approach. Useful to probably go through how to travel backwards in a string. 

def romanToInt(s):
    # O(N) time complexity where N is the number of elements in the string
    # O(N) space complexity where N is the number of roman numerals we have
    # create the dictionary
    roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    z = 0
    for i in range(0, len(s) - 1):
        if roman[s[i]] < roman[s[i + 1]]:
            z -= roman[s[i]]
        else:
            z += roman[s[i]]
    return z + roman[s[-1]]

# using a dictionary and travelling backwards
# this was very difficult to wrap my head around 
def romanToInt2(s):
    # this is a lot faser for some reason
    #O(N) time complexity where N is the number of elements in the string
    # O(N + M) space complexity where N is the number of roman numerals we have in the dictionarya nd M is the number of elements in the string i.e. s[::-1] creates a new copy
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    prev = 0
    sum = 0

    for i in s[::-1]:
        curr = roman[i]
        if prev > curr:
            sum -= curr
        else:
            sum += curr
        prev = curr
    return sum

# retried 21/01
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        if len(s) == 1:
            return roman_dict[s]
        
        result = 0
        
        for i in range(0, len(s) - 1):
            if roman_dict[s[i]] < roman_dict[s[i+1]]:
                result -= roman_dict[s[i]]
            else:
                result += roman_dict[s[i]]
        return result + roman_dict[s[-1]]