class Node:
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data
  
  def inorder(self):
    if self.left:
      self.left.inorder()
    print(self.data, end=' ')
    if self.right:
      self.right.inorder()

  def preorder(self):
    # visiting the root node
    print(self.data, end=' ')

    # visiting the left subtree
    if self.left:
      self.left.preorder()

    # visiting the right subtree
    if self.right:
      self.right.preorder()

  def postorder(self):
    # add implementation for postorder
    if self.left:
      self.left.postorder()
    if self.right:
      self.right.postorder()
    print(self.data, end=' ')
    pass

# create the root node
node = Node(1)

# add nodes
node.left  = Node(12)
node.right = Node(9)
node.left.left = Node(5)
node.left.right = Node(6)

# traverse inorder
#node.inorder()
#print()
#node.preorder()
node.postorder()
