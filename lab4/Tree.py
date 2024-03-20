class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None
    
    def isempty(self):
        return self.data == None
    
    def clear(self):
        self.data = None

    def search(self, target):
        if  self.data is None or self.data == target:
            return
        if self.data < target:
            return self.right.search(target)
        return self.left.search(target)
    
    def insert(self, data):
        if self.data is None:
            self.data = data
        elif self.data > data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
    
    # def breadth(self):
    #     if self.data is None:
    #         return
    #     lis = []
    #     lis.append(self.data)
    #     while lis:
    #         node = lis.pop(0)
    #         print(node.data, end = " ")
            
    #         if node.left:
    #             lis.append(node.left)
    #         if node.right:
    #             lis.append(node.right)


if __name__ == "__main__":
    bst = Node()
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)

    print("Breadth-first traversal of the BST:")
    bst.search(6)
