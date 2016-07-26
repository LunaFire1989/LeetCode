class Solution(object):
    def myAtoi(self, str):
        str = str.strip()
        if str.find(' ') != -1:
            str = str[:str.find(' ')]
        
        length = len(str)
        for i in range(1, length):
            if str[i - 1] >= '0' and str[i - 1] <= '9' and (str[i] < '0' or str[i] > '9'):
                str = str[:i]
                break
        
        try:
            result = int(str)
        except:
            return 0
            
        if result > 2147483647:
            result = 2147483647
        if result < -2147483648:
            result = -2147483648
        return result
        
solution = Solution()
result = solution.myAtoi('  123 456')
print result