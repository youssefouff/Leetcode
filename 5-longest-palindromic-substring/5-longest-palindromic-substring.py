class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome = ""
        palindromeLength = 0
        
        for i in range (len(s)):
            l , r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > palindromeLength:
                    palindrome = s[l:r+1]
                    palindromeLength = r-l+1
                l -= 1
                r += 1
                
            l , r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > palindromeLength:
                    palindrome = s[l:r+1]
                    palindromeLength = r-l+1
                l -= 1
                r += 1
        
        return palindrome
            
            
        
        
        
        
        
        
        
        
        
        
        
        
#han3ml eh ?
# han pass 3al string char by char 