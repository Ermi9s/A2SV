class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stck = [0]
        ans = 0
        heights.append(0)
        for i in range(len(heights)):
            while stck and heights[stck[-1]] > heights[i]:
                h = heights[stck.pop()]
                l = i if not stck else i - stck[-1] - 1
                ans = max(ans, h*l)
            stck.append(i)
        return ans