# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        if root and not root.left and not root.right and root.val == expectNumber:
            return [[root.val]]
        res = []
        left = self.FindPath(root.left, expectNumber-root.val)
        right = self.FindPath(root.right, expectNumber-root.val)
        for i in left+right:
            res.append([root.val]+i)
        return res

#print([[1],[2,3]]+[[4]])


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution2:
    def IsBalanced_Solution(self, root):
        # write code here
        if not root:
            return True
        if abs(self.maxdepth(root.left) - self.maxdepth(root.right)) > 1:
            return False
        return self.IsBalanced_Solution(root.left) and self.IsBalanced_Solution(root.right)

    def maxdepth(self, root):
        if not root:
            return 0
        left = self.maxdepth(root.left)
        right = self.maxdepth(root.right)
        return max(left + 1, right + 1)

# -*- coding:utf-8 -*-
class Solution3:
    def __init__(self):
        self.cnt = 0

    def movingCount(self, threshold, rows, cols):
        # write code here
        board = [[0 for x in range(cols)] for y in range(rows)]
        self.findway(0, 0, board, threshold)
        return self.cnt

    def findway(self, i, j, board, threshold):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        tmpi = list(map(int, list(str(i))))
        tmpj = list(map(int, list(str(j))))
        if sum(tmpi) + sum(tmpj) > threshold or board[i][j] == 1:
            return
        board[i][j] = 1
        self.cnt += 1
        self.findway(i + 1, j, board, threshold)
        self.findway(i - 1, j, board, threshold)
        self.findway(i, j - 1, board, threshold)
        self.findway(i, j + 1, board, threshold)

#S=Solution3()
#print(S.movingCount(5,10,10))

class Solution4:
    def deleteDuplication(self, pHead):
        # write code here
        cur=dummy=ListNode(0)
        dummy.next=pHead
        tmp=pHead
        while tmp and tmp.next:
            if tmp.val==tmp.next.val:
                while tmp.next and tmp.val==tmp.next.val:
                    tmp=tmp.next
            else:
                cur.next=tmp
                cur=cur.next
            tmp=tmp.next
        cur.next=tmp
        return dummy.next

class Solution5:
    # matrix类型为二维列表，需要返回列表
        def printMatrix(self, matrix):
            res = []
            while matrix:
                res += matrix.pop(0)
                if matrix and matrix[0]:
                    for row in matrix:
                        res.append(row.pop())
                if matrix:
                    res += matrix.pop()[::-1]
                if matrix and matrix[0]:
                    for row in matrix[::-1]:
                        res.append(row.pop(0))
            return res

class Solution6:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def push(self, node):
        # write code here
        self.stack1.append(node)
    def pop(self):
        # return xx
        if self.stack2==[]:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        return self.stack2.pop()

class Solution7:
    def reOrderArray(self, nums):
        # write code here
        for i in range(len(nums)):
            for j in range(len(nums)-1,i,-1):
                if nums[j]%2==1 and nums[j-1]%2==0:
                    nums[j],nums[j-1]=nums[j-1],nums[j]
        return nums

s7=Solution7()
a=[1,2,3,4,5,6,7,8,9,10]
print(s7.reOrderArray(a))

class Solution:
    def minNumberInRotateArray(self, nums):
        # write code here
        low=0
        high=len(nums)-1
        while low<high:
            mid=(high+low)//2
            if nums[mid]>nums[high]:
                low=mid+1
            elif nums[mid]==nums[high]:
                high=high-1
            else:
                high=mid
        return nums[low]



# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not pushV or len(pushV) != len(popV):
            return False
        stack = []
        for i in pushV:
            stack.append(i)
            while len(stack) and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
        if len(stack):
            return False
        return True
    
#二叉搜索树后续遍历
# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        length = len(sequence)
        if length == 0:
            return False
        if length == 1:
            return True
        root = sequence[-1]
        left = 0
        while sequence[left] < root:
                left += 1
        for j in range(left, length-1):
            if sequence[j] < root:
                return False
        return self.VerifySquenceOfBST(sequence[:left]) or self.VerifySquenceOfBST(sequence[left:length-1])

class Solution10:
    def MoreThanHalfNum_Solution(self, nums):
        # write code here
        dic={}
        length=len(nums)/2
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]]+=1
            else:
                dic[nums[i]]=1
        for i,j in dic.items():
            if j>length:
                return i
        return 0

S=Solution10()
a=[1,2,2,2,2,3,4]
print(S.MoreThanHalfNum_Solution(a))

class Solution11:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        cnt=0
        for i in range(1,n+1):
            tmpi=list(map(int,list(str(i))))
            for j in range(tmpi):
                if j==1:
                    cnt+=1
        return cnt

# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ""
        lmb = lambda n1, n2:int(str(n1)+str(n2))-int(str(n2)+str(n1))
        array = sorted(numbers, cmp=lmb)
        return ''.join([str(i) for i in array])

# -*- coding:utf-8 -*-
import collections
class Solution20:
    def FirstNotRepeatingChar(self, s):
        # write code herefor i in line:
        dic=collections.Counter(s)
        for i in s:
            if dic[i]==1:
                return i
        return -1

S=Solution20()
s='aaaaadbbbbbbbc'
print(S.FirstNotRepeatingChar(s))

class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        high=2
        low=1
        allres=[]
        while high>low:
            cur=(high+low)*(high-low+1)/2
            if cur<tsum:
                high+=1
            if cur==tsum:
                res=[]
                for i in range(low,high+1):
                    res.append(i)
                allres.append(res)
                low+=1
            if cur>tsum:
                low+=1
        return allres

class Solution30:
    def LeftRotateString(self, s, n):
        # write code here
        string=list(s)
        def reverse(s,left,right):
            while left<right:
                string[left],string[right]=string[right],string[left]
                left+=1
                right-=1
        reverse(s,0,n-1)
        reverse(s,n,len(s)-1)
        reverse(s,0,len(s)-1)
        return ''.join(i for i in string)

s='abcXYZdef'
S=Solution30()
print(S.LeftRotateString(s,4))

class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return pNode
        if pNode.right:
            left1=pNode.right
            while left1.left:
                   left1=left1.left
            return left1
        p=pNode
        while pNode.next:
            tmp=pNode.next
            if tmp.left==pNode:
                return tmp
            pNode=tmp