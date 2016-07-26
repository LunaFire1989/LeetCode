class Solution(object):
    def reverse(self, x):
        table, flag = [], False
        if x < 0:
            flag = True
            x *= -1

        while x != 0:
            table.append(x % 10)
            x /= 10
        result = 0
        for v in table:
            result = result * 10 + v
        if flag:
            result *= -1
            
        if result < -2147483648 or result > 2147483647:  
              return 0
        return result

solution = Solution()
result = solution.reverse(0)
print result