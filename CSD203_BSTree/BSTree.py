def f0():
    return print('HE181861')

class Bird:
    def __init__(self, bird_type, rate, wing):
        self.type = bird_type
        self.rate = rate
        self.wing = wing
    
    def __str__(self):
        return f"({self.type}, {self.rate}, {self.wing})"

class Node:
    def __init__(self, bird):
        self.bird = bird
        self.left = None
        self.right = None

class BSTree:
    def __init__(self):
        self.root = None

    def insert(self, bird):
        if not isinstance(bird, Bird):
            return ValueError("Invalid bird object")
        
        if bird.type[0] == 'B'  or bird.rate > 10:
            return
        else:
            if self.root is None:
                self.root = Node(bird)
            else:
                self.insert_recursive(self.root, bird)
    
    def insert_recursive(self, current_node, bird):
        if bird.rate < current_node.bird.rate:
            if current_node.left is None:
                current_node.left = Node(bird)
            else:
                self.insert_recursive(current_node.left, bird)
        
        elif bird.rate > current_node.bird.rate:
            if current_node.right is None:
                current_node.right = Node(bird)
            else:
                self.insert_recursive(current_node.right, bird)
        
        else:
            pass
    
    def preorder_traversal(self):
        if self.root is None:
            print("Tree is empty")
        else:
            self._preorder_recursive(self.root)

    def _preorder_recursive(self, current_node):
        if current_node is not None and current_node.bird.rate in range(4, 11):
            print(current_node.bird, end = ' ')
            self._preorder_recursive(current_node.left)
            self._preorder_recursive(current_node.right)

    def breadth_first_traversal(self):
        if self.root is None:
            print("Tree is None")
        else:
            self._breadth_first_traversal(self.root)
    
    def _breadth_first_traversal(self, current_node):
        lis = []
        lis.append(current_node)
        while lis:
            node = lis.pop(0)
            print(node.bird, end = '\n')

            if node.left is not None:
                lis.append(node.left)
            if node.right is not None:
                lis.append(node.right)

    def post_order(self):
        if self.root is None:
            return print("Tree is none")
        else:
            self._post_order(self.root)
    
    def _post_order(self, current_node):
        if current_node is not None:
            self._post_order(current_node.left)
            self._post_order(current_node.right)
            if current_node.bird.wing <= 4 and current_node.bird.rate > 6:
                print(current_node.bird, end ='\n')

    def in_order(self):
        if self.root is None:
            return print("Tree is none")
        else:
            self._in_order(self.root)
    
    def _in_order(self, current_node):
        if current_node is not None:
            self._in_order(current_node.left)
            if current_node.bird.type[0] == "A" or current_node.bird.type[0] == "C":
                print(current_node.bird, end = '\n')
            self._in_order(current_node.right)
    
    def f6():
        

if __name__ == '__main__':
    tree = BSTree()

    bird3 = Bird("Crow", 5, 2)
    bird1 = Bird("Sparrow", 10, 2)
    bird2 = Bird("Eagle", 20, 3)
    bird4 = Bird("Flamingo", 3, 12)
    bird5 = Bird("Parrot", 1, 8)
    bird6 = Bird("Vulture", 6, 22)
    bird7 = Bird("Antbird", 7, 11)

    tree.insert(bird3)
    tree.insert(bird1)
    tree.insert(bird2)
    tree.insert(bird4)
    tree.insert(bird5)
    tree.insert(bird6)
    tree.insert(bird7)

    tree.in_order()



