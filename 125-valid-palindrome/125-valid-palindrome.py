import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = re.sub("[^a-z|^0-9]","",s.lower())
        l = 0
        r = len(newString)-1
        while l < r:
            if newString[l] != newString[r]:
                return False
            l+=1
            r-=1
        return True
                
                
        