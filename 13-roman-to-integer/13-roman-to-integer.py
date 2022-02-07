class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {'I':1, 'V':5, 'X':10,
                         'L':50, 'C':100, 'D':500,
                         'M':1000}
        output = 0
        for i in range(0, len(s)-1):
            current_number = roman_numerals.get(s[i])
            next_number = roman_numerals.get(s[i+1])
            print(current_number)
            print(next_number)
            print('\n')
            if current_number < next_number:
                output -= current_number
            else:
                output += roman_numerals.get(s[i])
        return output + roman_numerals.get(s[-1])
