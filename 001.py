class Solution(object):
	def twoSum(self, nums, target):
		table = {v : i for i, v in enumerate(nums)}
		for i, v in enumerate(nums):
			if table.has_key(target - v) and table[target - v] != i:
				return [i, table[target - v]]
		return [0, 0]
	
solution = Solution()
result = solution.twoSum([0, 4, 3, 0], 0)
print result