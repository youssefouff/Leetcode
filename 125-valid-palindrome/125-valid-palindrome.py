import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #convert all upper to lower
        #remove all non alphanumeric characters
        newString=re.sub(r'[\W_]+', '', s.lower())
         
        l=0
        r=len(newString) - 1
        while l < r:
            if newString[l] != newString[r]:
                    return False
            
            l+=1
            r-=1
        return True
                
        