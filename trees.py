class node():
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
def printpreorder(root):
    if root==None:
        return
    print(root.data)
    printpreorder(root.left)
    printpreorder(root.right)
def printinorder(root):
    if root==None:
        return
    printpreorder(root.left)
    print(root.data)
    printpreorder(root.right)
def printpostorder(root):
    if root==None:
        return
    printpreorder(root.left)
    printpreorder(root.right)
    print(root.data)    
obj1=node(100)
obj2=node(21)
obj3=node(-151)
obj4=node(87)
obj5=node(12)
obj6=node(52)
obj7=node(8)
obj8=node(27)
obj9=node(28)
obj10=node(7)

obj1.left=obj2
obj1.right=obj3
obj2.left=obj4
obj2.right=obj5
obj3.left=obj6
obj3.right=obj7
obj4.right=obj8
obj5.right=obj9
obj7.left=obj10
print('preorder')
printpreorder(obj1)
print('inorder')
printinorder(obj1)
print('postorder')
printpostorder(obj1)

