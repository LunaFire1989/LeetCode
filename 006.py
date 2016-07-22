class Solution(object):
    def convert(self, s, numRows):
        table = []
        for i in range(numRows):
            table.append('')
        pos, length = 0, len(s)
        while pos < length:
            idx = 0
            while idx < numRows and pos < length:
                table[idx] += s[pos]
                idx += 1
                pos += 1
            idx = numRows - 2
            while idx >= 1 and pos < length:
                table[idx] += s[pos]
                idx -= 1
                pos += 1
        result = ''
        for i in range(numRows):
            result += table[i]
        return result
    
solution = Solution()
result = solution.convert('PAYPALISHIRING', 5)
print result