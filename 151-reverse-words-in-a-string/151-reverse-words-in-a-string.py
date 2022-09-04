class Solution:
    def reverseWords(self, s: str) -> str:
        #pointer to the words not the characters
        reverse = ''
        i = 0
        while i < len(s):
            while i< len(s) and s[i] == ' ':
                i+=1
            if i >= len(s):
                break
            j = i+1
            while j < len(s) and s[j] != ' ':
                j+=1
            word = s[i:j]
            if len(reverse) == 0:
                reverse = word
            else:
                reverse = word + ' ' + reverse
            i = j+1
        return reverse
                