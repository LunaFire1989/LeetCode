class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        
        nums = []
        while x != 0:
            nums.append(x % 10)
            x /= 10
        result = True
        for i in range(len(nums) / 2):
            if nums[i] != nums[len(nums) - 1 - i]:
                result = False
        return result
        
solution = Solution()
result = solution.isPalindrome(1001)
print result