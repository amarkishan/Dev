class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
def Inorder(root):
    stack=[]
    while(1):
        if root is not  None:
            stack.append(root)
            root=root.left
        elif(stack):
            root=stack.pop()
            print(root.data)
            root=root.right
        else:
           break

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)

Inorder(root)
