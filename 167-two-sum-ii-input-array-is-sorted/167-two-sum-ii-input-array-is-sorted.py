class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        output = []
        l=0
        r=len(numbers)-1
        while l < r:
            if numbers[l] + numbers[r] < target:
                l+=1
            elif numbers[l] + numbers[r] > target:
                r-=1
            else:
                output.extend([l+1, r+1])
                return output
                
        