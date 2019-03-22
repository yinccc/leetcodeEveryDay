class BinaryTree:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class Solution:
    def inorderTraversal(self,root,output):
        if root==None:
            return

        self.inorderTraversal(root.left,output)
        output.append(root.val)
        self.inorderTraversal(root.right,output)

    def ValidBinarySearchTree(self,root):
        output=[]

        self.inorderTraversal(root,output)
        for i in range(1,len(output)):
            if output[i-1]>=output[i]:
                return False
        return True

a=BinaryTree(1)
b=BinaryTree(2)
c=BinaryTree(3)
a.left=b
a.right=c
S=Solution()
print(S.ValidBinarySearchTree(a))

####################review Unique Binary Search Tree################
class Solution2:
    def UniqeBinarySearchTree(self,n):
        res=[0]*(n+1)
        res[0]=1
        for i in range(1,n+1):
            for j in range(i):
                res[i]+=(res[j]*res[i-j-1])
        return res

S2=Solution2()
print(S2.UniqeBinarySearchTree(15))


