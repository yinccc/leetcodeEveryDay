class Solution:
    def decodeString(self, s: str) -> str:
        stack_nums, stack_words, result, num = [], [], '', ''
        for ch in s:
            if ch.isdigit():
                num += ch
            elif ch == '[':
                stack_words.append(result)
                stack_nums.append(int(num))
                result, num = '', ''
            elif ch == ']':
                result = stack_words.pop() + stack_nums.pop() * result
            else:
                result += ch
        return result

S=Solution()
string='2[abc]3[cd]ef'
print(S.decodeString(string))