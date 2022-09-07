class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n = bin(n).replace("0b","")
        print(n)
        for i in range(1,(len(n))):
            if n[i] != n[i-1]:
                continue
            else:
                return False
        return True
        
        