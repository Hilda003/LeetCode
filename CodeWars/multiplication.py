# This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.
class Solution:
    def multiplication(number):
        
        return number * 8 if number % 2 == 0 else number * 9
    
    print(multiplication(4))
    print(multiplication(3))