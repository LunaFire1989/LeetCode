class Solution(object):
    def maxSubArray(self, nums):
        result, temp, length = nums[0], 0, len(nums)
        for i in range(length):
            temp = max(temp, 0)
            temp += nums[i]
            result = max(temp, result)
        return result
        
        
solution = Solution()
result = solution.maxSubArray([1, -2, 3, 4, 5, -10])
print result