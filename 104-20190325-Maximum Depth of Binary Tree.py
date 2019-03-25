class BinaryTree:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class Solution:
    def MaximumDepth(self,root):
        self.height=0
        def setDepth(root,height):
            if root:
                if self.height<height:
                    self.height=height
                setDepth(root.left,height+1)
                setDepth(root.right,height+1)
        setDepth(root,self.height+1)
        return self.height


a=BinaryTree(0)
b=BinaryTree(1)
c=BinaryTree(2)

a.left=b
b.left=c
S=Solution()
print(S.MaximumDepth(a))