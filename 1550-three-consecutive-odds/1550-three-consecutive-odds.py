class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        """
        left pointer at the first int and right pointer to the second int
        
        """
        if len(arr) < 3:
            return False
        count = 0
        for i in range(len(arr)):
            if arr[i] % 2 == 0:
                count = 0
                continue
            else:
                count+=1
                if count == 3:
                    return True
        return False
                
                
        