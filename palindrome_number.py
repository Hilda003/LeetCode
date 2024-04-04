class Solution:
    def isPalindrome(self, x:int) -> bool:
        
        # Konversi bilangan ke string
        str_x = str(x)

        # cek apakah nilai string akan sama jika dibalik
        return str_x == str_x[::-1]

solution = Solution()
print(solution.isPalindrome(132)) #False
