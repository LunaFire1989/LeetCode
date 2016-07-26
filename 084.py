class Solution(object):
    def largestRectangleArea(self, heights):
        heights.append(0)
        stk, result = [], 0
        for i in range(len(heights)):
            while(len(stk) != 0 and heights[stk[-1]] >= heights[i]):
                h = heights[stk.pop()]
                if len(stk) == 0:
                    s = i
                else:
                    s = i - stk[-1] - 1
                result = max(result, h * s)
            stk.append(i)
        return result

solution = Solution()
result = solution.largestRectangleArea([2, 1, 5, 6, 2, 3])
print result