class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        num, freq = 0, 0
        for n in nums:
            count[n]= 1 + count.get(n, 0)
            num = n if count[n] > freq else num
            freq = max(count[n], freq)
        return num