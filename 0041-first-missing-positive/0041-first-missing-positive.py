class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)
        
        i = 0
        while i < n:
            correct_pos = nums[i] - 1
            if 0 < nums[i] <= n and nums[i] != nums[correct_pos]:
                nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
            else:
                i += 1
        
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1