#Given a pre-order traversal history of a binary tree, check whether the path represents a valid BST or not. Return a string, either YES if the path can represent a valid BST, or NO if it cannot.
#
#Example 1:
#
#Input: "1 2 3 4 5 6 7"
#Output: "YES"
#Explanation: The path represents a valid BST.
#Example 2:
#
#Input: "1 2 3 4 5 6 7 8"
#Output: "YES"
#Explanation: The path represents a valid BST.
class BSTreeNode:
    def __init__(self, node_value):
        self.value = node_value
        self.left = self.right = None
    def insert(self, value):
        if self.left:
            self.insert()

def insert(node, data):
    if (data <= node.value):
        if node.left == None:
            node.left = BSTreeNode(data);
        else:
            node.left = insert(node.left, data)
        return node.left
    else:
        if node.right == None:
            node.right = BSTreeNode(data);
        else:
            node.right = insert(node.right, data)
        return node.right

def inorder(node):
    results = []
    if node.left:
        results.extend(inorder(node.left))
    results.append(node.value)
    if node.right:
        results.extend(inorder(node.right))
    return results

def build_tree(L):
    root = BSTreeNode(L.pop(0))
    new_node = insert(root, L.pop(0))
    while L:
        new_node = insert(new_node, L.pop(0))
    return root

L = [2]
L_copy =[*L]
root = build_tree(L)
results = (inorder(root))
L_copy.sort()
print('YES' if L_copy == results else 'NO')