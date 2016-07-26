class Solution(object):
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        result = 0
        while(left < right):
            result = max(result, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return result
        
solution = Solution()
result = solution.maxArea([1, 3, 5, 7, 1])
print result