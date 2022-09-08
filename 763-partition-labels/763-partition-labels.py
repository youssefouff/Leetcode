class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
            map each char to its last index
        
        """
        indexMap = {}
        
        for i, c in enumerate(s):
            indexMap[c] = i
        output = []
        size = 0
        start, end = 0, 0
        for i, c in enumerate(s):
            size+=1
            end = max(end, indexMap[c])
            if i == end:
                output.append(size)
                size = 0
        return output
        