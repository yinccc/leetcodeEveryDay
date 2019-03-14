class Solution(object):
    def combinationSum(self, candidates, target):
        result = []
        candidates = sorted(candidates)

        def dfs(remain, stack):
            if remain == 0:
                result.append(stack)
                return

            for item in candidates:
                if item > remain: break
                if stack and item < stack[-1]:
                    continue
                else:
                    dfs(remain - item, stack + [item])

        dfs(target, [])
        return result


s=Solution()
print(s.combinationSum([1,2,58,483,546,545,423321,545,323,6454],60))

