class Solution(object):
    def maxArea(self, height):
        start = 0
        end = len(height) - 1
        m = 0
        while start < end:
            res = min(height[start], height[end]) * (end - start)
            if res > m:
                m = res
            if height[start] < height[end] :
                start += 1
            else:
                end -= 1
        return m