class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        left pointer for a unique integer and right pointer to scan the array
        if nums[r] = nums[r-1] -> this is a duplicate so r+=1, 
        else nums[l] = nums[r] and l++
    
        """
        l, r = 1, 1
        while r < len(nums):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l+=1
            r+=1
        return l
                
        
        