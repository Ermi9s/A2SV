class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def maxHistogramRectangleArea(heights):
            area = 0
            stack = []
            for i, h in enumerate(heights):
                start = i
                while stack and stack[-1][1] > h:
                    index , height = stack.pop()
                    area = max(area,height * (i-index))
                    start = index
                    
                stack.append((start,h))
                
            for i,h in stack:
                
                area = max(area, h * (len(heights) - i))
                
            return area
        
        
        if not matrix: 
            return 0
        
        n = len(matrix[0])
        
        hist = [0] * (n)
        
        res = 0
        
        for row in matrix:
            for i in range(n):
                
                if row[i] == "1": 
                    hist[i] += 1
                    
                else: 
                    hist[i]=0
                    
            
            res = max(res, maxHistogramRectangleArea(hist))
            
        return res
	