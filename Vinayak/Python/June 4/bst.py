class BinarySearchTree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def addchild(self,data):
        if data==self.data:
            return

        if data<self.data:
            if self.left:
                self.left.addchild(data)
            else:
                self.left=BinarySearchTree(data)
        else:
            if self.right:
                self.right.addchild(data)
            else:
                self.right=BinarySearchTree(data)
    def inorder(self):
        elements=[]
        if self.left:
            elements+=self.left.inorder()
        
        elements.append(self.data)
        if self.right:
            elements+=self.right.inorder()
        
        return elements

def build_tree(elements):
    root=BinarySearchTree(elements[0])
    for i in range(1,len(elements)):
        root.addchild(elements[i])
    return root
        
numbers=[17,4,1,52,9,23,14,97]
numbers_tree=build_tree(numbers)
print(numbers_tree.inorder())





        

