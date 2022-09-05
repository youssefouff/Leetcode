class Solution:
    def romanToInt(self, s: str) -> int:
        romanSet={
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }
        output = 0
        for i in range (len(s)):
            if i+1 < len(s) and romanSet[s[i]] < romanSet[s[i+1]]:
                output-=romanSet[s[i]]
            else:
                output+=romanSet[s[i]]
        return output
            
        