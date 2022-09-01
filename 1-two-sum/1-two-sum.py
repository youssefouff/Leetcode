class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i in range (len(nums)):
            complement = target - nums[i]
            if complement not in hash_table:
                hash_table[nums[i]] = i
            else:
                return (hash_table[complement],i)
            
                    
            
                