class Solution:
    def removeDuplicates(nums):
        if len(nums) == 0:
            return 0
        index = 0
        
        # Iterate through the array
        for i in range(1, len(nums)):
            # If current element is different from previous unique element
            if nums[i] != nums[index]:
                # Move the unique index pointer forward
                index += 1
                nums[index] = nums[i]

        return index + 1