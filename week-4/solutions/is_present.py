class BSTreeNode:
    def __init__(self, node_value):
        self.value = node_value
        self.left = self.right = None

def _insert_node_into_binarysearchtree(node, data):
    if node == None:
        node = BSTreeNode(data)
    else:
        if (data <= node.value):
            node.left = _insert_node_into_binarysearchtree(node.left, data);
        else:
            node.right = _insert_node_into_binarysearchtree(node.right, data);
    return node
    
def isPresent (root,val):
  # write your code here
  # return 1 or 0 depending on whether the element is present in the tree or not
  if val < root.value:
    if root.left is None:
      return 0
    else:
      return isPresent(root.left, val)
  elif val > root.value:
    if root.right is None:
      return 0
    else:
      return isPresent(root.right, val)
  else: return 1