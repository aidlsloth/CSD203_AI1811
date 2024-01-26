class node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def evaluateExpressionTree(root):
    if root is None:
        return 0
    
    if root.left is None and root.right is None:
        return int(root.value)
    
    left_sum = evaluateExpressionTree(root.left)
    right_sum = evaluateExpressionTree(root.right)

    if root.value == '+':
        return left_sum + right_sum
    
    elif root.value == '-':
        return left_sum - right_sum
    
    elif root.value == '*':
        return left_sum * right_sum
    
    else:
        return left_sum // right_sum


if __name__ ==  "__main__":
    root = node('+')
    root.left = node('*')
    root.left.left = node('5')
    root.left.right = node('-4')
    root.right = node('-')
    root.right.left = node('100')
    root.right.right = node('20')
    print(evaluateExpressionTree(root))
    
        