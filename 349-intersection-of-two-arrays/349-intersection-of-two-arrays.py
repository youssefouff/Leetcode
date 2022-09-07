class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c = Counter(nums1)
        output = []
        for n in nums2:
            if c[n] > 0:
                if n not in output:
                    output.append(n)
                c[n]-=1
        return output