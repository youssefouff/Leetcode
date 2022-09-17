class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1:
            return 1
        pLength = 0
        c = Counter(s)
        
        for count in c.values():
            pLength += int(count/2)*2
            if pLength % 2 == 0 and count % 2  == 1:
                pLength+=1
        return pLength
        
        