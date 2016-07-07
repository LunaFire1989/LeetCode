class Solution(object):
	def findKthNumber(self, nums1, nums2, k):
		l1, l2 = len(nums1), len(nums2)
		if l1 == 0:
			return nums2[k - 1]
		if l2 == 0:
			return nums1[k - 1]
		
		mid1, mid2 = l1 / 2, l2 / 2
		if nums1[mid1] >= nums2[mid2]:
			if k >= mid1 + mid2 + 2:
				return self.findKthNumber(nums1, nums2[mid2 + 1:], k - (mid2 + 1))
			else:
				return self.findKthNumber(nums1[:mid1], nums2, k)
		else:
			if k >= mid1 + mid2 + 2:
				return self.findKthNumber(nums1[mid1 + 1:], nums2, k - (mid1 + 1))
			else:
				return self.findKthNumber(nums1, nums2[:mid2], k)
		
	
	def findMedianSortedArrays(self, nums1, nums2):
		totalLen = len(nums1) + len(nums2)
		if totalLen % 2 == 1:
			result = self.findKthNumber(nums1, nums2, totalLen / 2 + 1)
		else:
			result = (self.findKthNumber(nums1, nums2, totalLen / 2) + self.findKthNumber(nums1, nums2, totalLen / 2 + 1)) / 2.0
		return result
		
solution = Solution()
result = solution.findMedianSortedArrays([2], [5])
print result