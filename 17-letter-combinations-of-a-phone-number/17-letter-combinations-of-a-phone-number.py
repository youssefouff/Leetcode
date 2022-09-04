class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #map each digit to corresponding values
        map = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        if digits=='':
            return []
        numbers = list(map[digits[0]])
        
        for digit in digits[1:]:
            numbers = [old+new for old in numbers for new in list(map[digit])]
        
        return numbers