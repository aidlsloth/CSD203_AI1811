def f0():
    return print('HE181861')

class Bird:
    def __init__(self, bird_type='', rate=-1, wing=-1):
        self.type = bird_type
        self.rate = rate
        self.wing = wing
    
    def __repr__(self):
        return f"({self.type}, {self.rate}, {self.wing})"

class Node:
    def __init__(self, bird):
        self.bird = bird
        self.left = None
        self.right = None

class BSTree:
    def __init__(self):
        self.root = None
    
    def clear(self):
        self.root = None
    
    def isEmpty(self):
        return self.root == None

    def preOrder(self, p):
        if p == None:
            return
        self.visit(p)
        self.preOrder(p.left)
        self.preOrder(p.right)
    
    def preVisit(self):
        self.preOrder(self.root)
        print("")
    def visit(self, p):
        if p == None:
            return
        print(f"{p.bird}", end = " ")

    def postOrder(self, p):
        if p == None:
            return
        self.postOrder(p.left)
        self.postOrder(p.right)
        self.visit(p)
    def postVisit(self):
        self.postOrder(self.root)
        print("")
    
    def inOrder(self, p):
        if p == None:
            return
        self.inOrder(p.left)
        self.visit(p)
        self.inOrder(p.right)
    def inVisit(self):
        self.inOrder(self.root)
        print('')

    def insert(self, bird_type, rate, wing):
        if bird_type[0] == 'B'  or rate > 10:
            return
        nbird = Node(Bird(bird_type, rate, wing))
        if self.root is None:
            self.root = nbird
            return
        cur = self.root
        father = None
        while cur:
            if cur.bird.rate == rate:
                return
            else:
                father = cur
                if cur.bird.rate < rate:
                    cur = cur.right
                else:
                    cur = cur.left
        if father.bird.rate < rate:
            father.right = nbird
        else:
            father.left = nbird
    
    def pre_order1(self, p):
        if p == None:
            return
        if p.bird.wing in range(4, 11):
            self.visit(p)
        self.pre_order1(p.left)
        self.pre_order1(p.right)
    def pre_visit1(self):
        self.pre_order1(self.root)
        print("")

    def breadth_first(self):
        if self.isEmpty():
            return
        lis = []
        count = 1
        lis.append(self.root)
        while lis:
            node = lis.pop(0)
            if count % 2 != 0:
                self.visit(node)
            count += 1 
            if node.left != None:
                lis.append(node.left)
            if node.right != None:
                lis.append(node.right)
    
    def post_order2(self, p):
        if p == None:
            return
        self.post_order2(p.left)
        self.post_order2(p.right)
        if p.bird.wing <= 4 or p.bird.rate >6:
            self.visit(p)
    def post_visit2(self):
        self.post_order2(self.root)
    
    def in_order2(self, p):
        if p == None:
            return
        self.in_order2(p.left)
        if p.bird.type[0] == 'A' or p.bird.type [0] == 'C':
            self.visit(p)
        self.in_order2(p.right)
    def post_visit2(self):
        self.in_order2(self.root)

    def deleteFatherByMerging(self):
        counter = 0
        self.findthirdnode(self.root, counter, None)
    def findthirdnode(self, node, counter, parent):
        if node is None:
            return
        self.findthirdnode(node.left, counter, node)
        counter += 1
        if counter == 3:
            self.mergeAndDelete(parent)
        self.findthirdnode(node.right, counter, node)
    
    def mergeAndDelete(self, p):
        if p is None:
            return
        mergedSubtree = self.merge(p.left, p.right)
        if p is self.root:
            self.root = mergedSubtree
        elif p is p.left:
            p.left = mergedSubtree
        else:
            p.right = mergedSubtree

    def merge(self, left, right):
        if left is None:
            return right
        if right is None:
            return left
        rightmost = self.findrightmost(left)
        rightmost.right = right
        return left
    
    def findrightmost(self, p):
        while p.right is not None:
            p = p.right
        return p
if __name__ == '__main__':
    tree = BSTree()
    tree.clear()

    tree.insert("A", 5, 9)
    tree.insert("E", 2, 5)
    tree.insert("B", 4, 32)
    tree.insert("C", 11, 12)
    tree.insert("D", 8, 6)
    tree.insert("F", -6, 7)
    tree.insert("X", 4, 5)
    tree.insert("y", 6, -7)

    tree.preVisit()
    tree.deleteFatherByMerging()
    tree.preVisit()



