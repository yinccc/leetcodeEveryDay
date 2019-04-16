class Solution:
    def invertBinaryTree(self,root):
        if root:
            root.left,root.right=self.invertBinaryTree(root.right),self.invertBinaryTree(root.left)
        return root


class BinaryTree:
    def __init__(self,x):
        self.val=x
        self.right=None
        self.left=None


a=BinaryTree(1)
b=BinaryTree(2)
c=BinaryTree(3)

a.left=b
a.right=c

S=Solution()
print(S.invertBinaryTree(a).left.val)
