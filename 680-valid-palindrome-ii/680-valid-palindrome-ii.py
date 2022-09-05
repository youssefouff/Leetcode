class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                removeL = s[l+1:r+1]
                removeR = s[l:r]
                return (removeL == removeL[::-1] or removeR == removeR[::-1])
            l+=1
            r-=1
        return True
            
                