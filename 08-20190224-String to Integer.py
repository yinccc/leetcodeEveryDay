class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str or len(str) < 1:
            return 0
        i = 0
        while str[i] == ' ':
            i += 1
        str = str[i:]
        j = 0
        sign = '+'
        if str[0] == '-':
            sign = '-'
            j += 1
        elif str[0] == '+':
            j += 1

        result = 0
        while len(str) > j and str[j] >= '0' and str[j] <= '9':
            result = result * 10 + (ord(str[j]) - ord('0'))
            j += 1
        if sign == '-':
            result = -result
        if result > 2147483647:
            return 2147483647
        elif result < -2147483648:
            return -2147483648
        else:
            return result

s=Solution()
print(s.myAtoi('  -42'))