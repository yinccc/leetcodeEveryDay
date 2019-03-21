class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None


def BinaryTreeInorderTraversal(root):
    res=[]
    helper(root,res)
    return res



def helper(root,res):
    if root:
        helper(root.left,res)
        res.append(root.val)
        helper(root.right,res)


a=TreeNode(1)
b=TreeNode(2)
c=TreeNode(3)
a.left=b
a.right=c

print(BinaryTreeInorderTraversal(a))