class Solution(object):
    def isValid(self, s):
        """
        :type s: str;; rtype: bool
        """
        stack = []
        for p in s:
            if p in '[({': stack.append(p)
            else:
                if not stack: return False
                elif p == ']' and stack.pop() != '[':
                    return False
                elif p == ')' and stack.pop() != '(':
                    return False
                elif p == '}' and stack.pop() != '{':
                    return False
        return (stack == [])

S=Solution()
S.isValid('{([])}')