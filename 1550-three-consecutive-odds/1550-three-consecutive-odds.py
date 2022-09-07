class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        """
         count number of odds and once I reach count = 3 return true
        
        """
        if len(arr) < 3:
            return False
        count = 0
        for i in range(len(arr)):
            if arr[i] % 2 == 1:
                count += 1
            else:
                count = 0
            if count == 3:
                return True
        return False
                
                
        