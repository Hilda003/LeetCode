from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in num_dict:
                return [num_dict[complement], i]
            

            num_dict[num] = i
        
        return None
    

solution = Solution()
nums1 = [2, 7, 11, 15]
target1 = 9
print(solution.twoSum(nums1, target1))