class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = "{:b}".format((x^y))
        count = 0
        for bit in xor:
            count+= int(bit)
        return count
            