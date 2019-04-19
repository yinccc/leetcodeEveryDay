class BinaryTree:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None


class Solution:
    def lowestCommonAncestorTree(self,root,p,q):
        if not root:
            return None
        if root==p or root==q:
            return root

        #divide
        left=self.lowestCommonAncestorTree(root.left,p,q)
        right=self.lowestCommonAncestorTree(root.right,p,q)

        #conquer
        if left and right:
            return root
        if not left:
            return right
        if not right:
            return left


a=BinaryTree(3)
b=BinaryTree(5)
c=BinaryTree(6)
d=BinaryTree(2)
e=BinaryTree(7)
f=BinaryTree(4)

h=BinaryTree(1)
i=BinaryTree(0)
j=BinaryTree(8)

a.left=b
a.right=h

b.left=c
b.right=d

h.left=i
h.right=j

d.left=e
d.right=f

S=Solution()
print(S.lowestCommonAncestorTree(a,f,e).val)

print("00"+str(30))