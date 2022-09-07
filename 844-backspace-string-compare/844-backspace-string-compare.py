class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        newS = []
        newT = []
        
        for c in s:
            if c == "#":
                if newS:
                    newS.pop()
            else:
                newS.append(c)
        for c in t:
            if c == "#":
                if newT:
                    newT.pop()
            else:
                newT.append(c)
        if newS == newT:
            return True
        else:
            return False