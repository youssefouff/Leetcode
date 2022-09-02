class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        table = set(nums)
        longestSequence = 0
        for n in nums:
            if (n-1) not in table:
                length = 0
                while (n+length) in table:
                    length += 1
                    longestSequence = max(length, longestSequence)
        return longestSequence