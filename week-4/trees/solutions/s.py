#A binary tree uses a multi-node data structure where each node may have 0 to 2 child nodes, and has one stored value, its node number in this case. A tree may either be:

#    An empty tree, the root is null.
#    A non-empty tree with a non-null root node that contains a value and up to 2 subtrees, left and right, which are also binary trees.
#
# 
#
#A binary tree is classified as a binary search tree (BST) if all of the non-null nodes exhibit two properties:
#
#    The left subtree of each node contains only nodes with values that are lower than its own value.
#    The right subtree of each node contains only nodes with values that are higher than its own value.
#
# 
#
#A pre-order traversal is a recursive tree traversal method where the current node is visited first, then the left subtree, and then the right subtree. The following pseudocode parses a tree into a list using pre-order traversal:
#
#    If the root is null, return the null list.
#    For a non-null root node:
#        Create a pre-order traversal list, left, of the left subtree.
#        Create a pre-order traversal list, right, of the right subtree.
#        Return the concatenated list: the non-null node + left + right.
#
# 
#
#Given a pre-order traversal history of a binary tree, check whether the path represents a valid BST or not. Return a string, either YES if the path can represent a valid BST, or NO if it cannot.
#
# 
#
#Example
#
#nodes = [2, 1, 3, 4, 5]
#
# 
#
#    The root node will always be the first node in the array. In this case, the root is at node 2
#    The next value, 1 is less than 2. Place the node 1 at the left of node 2.
#    The next value, 3 is greater than 2. Place the node 3 at the right of node 2.
#    The next value, 4 is greater than 3. Place the node 4 at the right of node 3.
#    The next value, 5 is greater than 4. Place the node 5 at the right of node 4.
#    This graph meets the definition of a BST.

def is_bst(L):
    if not L:
        return True
    root = L[0]
    left = L[1: L.index(root)+1]
    right = L[L.index(root)+1:]
    return is_bst(left) and is_bst(right) and all(left[i] < root < left[i+1] for i in range(len(left)-1)) and all(right[i] > root > right[i+1] for i in range(len(right)-1))

L = [3,4,5,1,2]
print(is_bst(L))