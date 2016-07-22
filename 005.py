class Solution(object):
    def calcPalindromeRange(self, left, right, s):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1
    
    def longestPalindrome(self, s):
        length, result = 0, ''
        for i in range(len(s)):
            left, right = self.calcPalindromeRange(i, i, s)
            if right - left + 1 > length:
                length = right - left + 1
                result = s[left: right + 1]
            left, right = self.calcPalindromeRange(i, i + 1, s)
            if right - left + 1 > length:
                length = right - left + 1
                result = s[left: right + 1]
        return result
        
solution = Solution()
result = solution.longestPalindrome('abcbaaabbaa')
print result