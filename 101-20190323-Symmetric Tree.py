class BinaryTree:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class Solution:
    def SymmetricTree(self,root):
        def symm(left,right):
            if left and right:
                return left.val==right.val and symm(left.left,right.right) and symm(left.right,right.left)
            else:
                return left==right
        return symm(root,root)


a=BinaryTree(0)
b=BinaryTree(1)
c=BinaryTree(1)
a.left=b
a.right=c
S=Solution()
print(S.SymmetricTree(a))
