class Node:
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data
  
  def insert(self, data):
    if data < self.data:
      if self.left is None:
        self.left = Node(data)
      else:
        self.left.insert(data)
    elif data > self.data:
      if self.right is None:
        self.right = Node(data)
      else:
        self.right.insert(data)
    else:
      self.data = data

  def find(self, data):
    if self.data < data:
      if self.right is None:
        return None
      return self.right.find(data)
    elif self.data > data:
      if self.left is None:
        return None
      return self.left.find(data)
    else:
      return self

  def preorder(self):
    print(self.data, end=' ')
    if self.left:
      self.left.preorder()
    if self.right:
      self.right.preorder()

  def inorder(self):
    if self.left:
      self.left.inorder()
    print(self.data, end=' ')
    if self.right:
      self.right.inorder()

  def postorder(self):
    if self.left:
      self.left.postorder()
    if self.right:
      self.right.postorder()
    print(self.data, end=' ')
  
  def delete(self, item):
    pass

root = Node(1)
root.insert(12)
root.insert(5)
root.insert(6)
root.insert(9)

# find nodes
root.find(8)
root.find(10)
root.find(4)
root.find(9)

root.preorder()
print()
root.inorder()
print()
root.postorder()