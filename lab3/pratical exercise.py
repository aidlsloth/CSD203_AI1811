def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n-1)
    
def findmin(a, n):
    if n == 1:
        return a[0]
    rest = findmin(a[1:], n -1)
    if a[0] < rest:
        return a[0]
    else:
        return rest
    
# a = [3, 17, 1, 4, 9, 2]
# n = len(a)
# minE = findmin(a, n)
# print(minE)
    
def findsum(a, n):
    if n == 1:
        return a[0]
    else:
        return a[0] + findsum(a[1:], n - 1)
    
# a = [3, 17, 1, 4, 9, 2]
# n = len(a)
# total = findsum(a, n)
# print(total)

def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)
    
def fibonacci(n):
    if n <= 0:
        print("Incorrect input")

    elif n == 1:
        return 0
    
    elif n == 2:
        return 1
    
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def addReciprocals(n):
    if n == 0:
        print("Incorrect input")
    elif n == 1:
        return 1
    else:
        return 1/n + addReciprocals(n-1)
    
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)
    
def GCD(m, n):
    if n == 0:
        return m
    elif n > 0:
        return GCD(n, m%n)
    
def Stirlingnumb(n, k):
    if n == k == 0:
        return 1
    elif n > 0 and k == 0:
        return 0
    elif n == 0 or k > n:
        return 0
    return Stirlingnumb(n-1, k-1) - n*Stirlingnumb(n-1,k)
    
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def tree_height(root):
    if root is None:
        return 0
    else:
        left_height = tree_height(root.left)
        right_height = tree_height(root.right)
        return 1 + max(left_height, right_height)
    
def tree_size(root):
    if root is None:
        return 0
    
    else:
        left_size = tree_size(root.left)
        right_size = tree_size(root.right)
        return 1 + left_size + right_size
    
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.left.left = TreeNode(3)
# root.right = TreeNode(4)
# root.left.right = TreeNode(5)

# height = tree_height(root)
# size = tree_size(root)

# print("Height of binary tree: ", height)
# print("Size of binary tree: ", size)
    
def search(a, n, target):
    if n > 0:
        if a[0] == target:
            return True
        else: 
            return search(a[1:], n-1, target)
    else:
        return False
    






