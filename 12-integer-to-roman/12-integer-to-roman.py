class Solution:
    def intToRoman(self, num: int) -> str:
        romanInt = [
            ["I",1],
            ["IV",4],
            ["V",5],
            ["IX",9],
            ["X",10],
            ["XL",40],
            ["L",50],
            ["XC",90],
            ["C",100],
            ["CD",400],
            ["D",500],
            ["CM",900],
            ["M",1000]
        ]
        output = ""
        for rom, val in reversed(romanInt):
            if num // val:
                count = num //val
                output+= (rom * count)
                num = num % val
        return output
        