class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        current = 0
        for i in range (len(nums)):
            current += nums[i]
            if current - nums[i] == sum(nums) - current:
                return i
        return -1
        
        