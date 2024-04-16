class Solution:
    def square_sum (numbers):
        num = 0

        for i in numbers:
            num += i ** 2
        
        return num

    print(square_sum([2, 3]))