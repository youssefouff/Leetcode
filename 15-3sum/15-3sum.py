class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while l<r:
                target = nums[i] + nums[l] + nums[r]
                if target > 0:
                    r-=1
                elif target < 0:
                    l+=1
                else:
                    output.append((nums[i],nums[l],nums[r]))
                    l+=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
                    
                
                
        return output
                
            
            