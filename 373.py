class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        result = []
        len1, len2 = len(nums1), len(nums2)
        idx = [0 for i in range(len1)]
        for c in range(min(k, len1 * len2)):
            mx_val = nums1[-1] + nums2[-1]
            for i in range(len1):
                if idx[i] < len2 and nums1[i] + nums2[idx[i]] <= mx_val:
                    mx_val = nums1[i] + nums2[idx[i]]
                    pos = i
            result.append([nums1[pos], nums2[idx[pos]]])
            idx[pos] += 1
        return result
        
solution = Solution()
result = solution.kSmallestPairs([1,2,4,5,6], [3,4,7,9], 20)
print result
                    
                    
              
                