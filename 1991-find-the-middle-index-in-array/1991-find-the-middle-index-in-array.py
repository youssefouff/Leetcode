class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        currSum = sum(nums)
        curr = 0
        for i in range (len(nums)):
            curr += nums[i]
            if curr - nums[i] == currSum - curr:
                return i
        return -1
        
        