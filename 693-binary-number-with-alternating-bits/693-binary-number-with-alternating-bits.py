class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if n == 0:
            return True
        n = bin(n).replace("0b","")
        print(n)
        for i in range(1,(len(n))):
            if n[i] == n[i-1]:
                return False
        return True
            
        
        