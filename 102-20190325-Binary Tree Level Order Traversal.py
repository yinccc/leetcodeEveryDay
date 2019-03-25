class BinaryTree:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class Solution:
    def BinaryTreeLevelOrderTraversal(self,root):
        if not root:
            return []
        ans,level=[],[root]
        while level:
            ans.append([node.val for node in level])
            temp=[]
            for node in level:
                temp.extend([node.left,node.right])
            level=[leaf for leaf in temp if leaf]
        return ans

a=BinaryTree(0)
b=BinaryTree(1)
c=BinaryTree(2)
a.left=b
a.right=c
S=Solution()
print(S.BinaryTreeLevelOrderTraversal(a))
