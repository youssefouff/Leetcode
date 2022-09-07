class Solution:
    def countSegments(self, s: str) -> int:
        """
        if I'm on the first element of the string and it is not space then I start my count
        if I'm on an char which is space then continue, till I reach a non space character             then check if the prev char was a space the -> counter++
        
        """
        count = 0
        for i in range(len(s)):
            if (i == 0 or s[i-1] == " ") and s[i] != " ":
                count += 1
        return count