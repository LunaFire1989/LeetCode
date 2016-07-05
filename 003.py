class Solution(object):
	def lengthOfLongestSubstring(self, s):
		table, pos, result = {}, 0, 0
		for i, v in enumerate(s):
			if table.has_key(v):
				pos = max(table[v] + 1, pos)
			result = max(result, i - pos + 1)
			table[v] = i
		return result
		
s = ""
solution = Solution()
result = solution.lengthOfLongestSubstring(s)
print result