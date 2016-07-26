class Solution(object):
    def maximalRectangle(self, matrix):
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        
        nums = []
        for i in range(m):
            nums.append([])
            for j in range(n):
                nums[i].append(int(matrix[i][j]))
                if i > 0 and nums[i][j] > 0:
                    nums[i][j] += nums[i - 1][j]
        
        result = 0
        for i in range(m):
            stk = []
            for j in range(n + 1):
                while len(stk) != 0 and (j == n or nums[i][stk[-1]] >= nums[i][j]):
                    h = nums[i][stk.pop()]
                    if len(stk) == 0:
                        s = j
                    else:
                        s = j - stk[-1] - 1
                    result = max(result, h * s)
                stk.append(j)
        return result
        
solution = Solution()
result = solution.maximalRectangle(["10100","10111","11111","10010"])
print result