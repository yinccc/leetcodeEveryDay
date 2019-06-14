class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

a=TreeNode(1)
b=TreeNode(2)
c=TreeNode(3)
a.left=b
a.right=c


def preOrder(node):
    if node:
        print(node.val,end='')
        preOrder(node.left)
        preOrder(node.right)

def inOrder(node):
    if node:
        inOrder(node.left)
        print(node.val,end='')
        inOrder(node.right)

def reOrder(node):
    if node:
        reOrder(node.left)
        reOrder(node.right)
        print(node.val, end='')

def preOrder2(node):
    stack = [node]
    while len(stack) > 0:
        print(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        node = stack.pop()

#preOrder2(a)

def inOrder2(node):
    stack = []
    pos = node
    while pos or stack:
        if pos:
            stack.append(pos)
            pos = pos.left
        else:
            pos = stack.pop()
            print(pos.val)
            pos = pos.right

#inOrder2(a)

def reOrder2(node):
    stack = [node]
    stack2 = []
    while len(stack) > 0:
        node = stack.pop()
        stack2.append(node)
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)
    while len(stack2) > 0:
        print(stack2.pop().val)

#reOrder2(a)
print('----------------------------')
def qianxu(root):
    stack=[root]
    while stack:
        print(root.val)
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)
        root=stack.pop()

qianxu(a)

def zhongxu(root):
    stack=[]
    while stack or root:
        if root:
            stack.append(root)
            root=root.left
        else:
            root=stack.pop()
            print(root.val)
            root=root.right
print('----------------------------')
zhongxu(a)




