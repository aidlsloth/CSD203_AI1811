from collections import deque

class BinarySearchTree:
    class Node:
        def __init__(self, key):
            self.left = None
            self.right = None
            self.val = key

    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return self.Node(key)
        else:
            if root.val < key:
                root.right = self._insert(root.right, key)
            else:
                root.left = self._insert(root.left, key)
        return root

    def inorder_traversal(self):
        self._inorder_traversal(self.root)

    def _inorder_traversal(self, root):
        if root:
            self._inorder_traversal(root.left)
            print(root.val, end=" ")
            self._inorder_traversal(root.right)

    def clear(self):
        self.root = self._clear(self.root)

    def _clear(self, root):
        if root:
            root.left = self._clear(root.left)
            root.right = self._clear(root.right)
            root = None
        return root

    def search(self, x):
        return self._search(self.root, x)

    def _search(self, root, x):
        if root is None or root.val == x:
            return root
        if root.val < x:
            return self._search(root.right, x)
        return self._search(root.left, x)

    def breadth(self):
        if self.root is None:
            return

        queue = []
        queue.append(self.root)

        while queue:
            node = queue.pop(0)
            print(node.val, end=" ")

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

# Example usage:
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)

    print("Breadth-first traversal of the BST:")
    bst.breadth()
