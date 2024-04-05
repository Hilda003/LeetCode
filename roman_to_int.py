class Solution:
    def romanToInt(s: str) -> int:
        # memetakan setiap simbol Romawi ke nilai numerik

        roman_value = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 100

        }

        # Inisialisasi variable total = 0
        total = 0

        # Iterasi setiap karakter
        for i in range(len(s)):
            if i < len(s) - 1 and roman_value[s[i]] < roman_value[s[i+1]]:
                total -= roman_value[s[i]]
            else:
                total += roman_value[s[i]]
        # return total
        return total
    
    print(romanToInt("III"))