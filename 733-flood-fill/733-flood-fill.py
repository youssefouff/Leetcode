class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        color = image[sr][sc]
        if color != newColor:
            image = self.fill(image, sr, sc, newColor, color)
        return image
    
    
    def fill(self, image: List[List[int]], sr: int, sc: int, newColor: int, color: int) -> List[List[int]]:
        if 0 <= sr < len(image) and 0 <= sc < len(image[0]):
            if image[sr][sc] == color:
                image[sr][sc] = newColor
                
                image = self.fill(image, sr - 1, sc, newColor, color)
                image = self.fill(image, sr, sc + 1, newColor, color)
                image = self.fill(image, sr + 1, sc, newColor, color)
                image = self.fill(image, sr, sc - 1, newColor, color)
        
        return image