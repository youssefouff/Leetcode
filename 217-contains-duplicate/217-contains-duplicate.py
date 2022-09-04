class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #create hashset and add non repeated integers of nums
        #if repeated -> true, else -> false
        
        hashSet = set()
        for n in nums:
            if n in hashSet:
                return True
            hashSet.add(n)
        return False
        