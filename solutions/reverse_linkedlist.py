class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

  def __repr__(self) -> str:
      return "Node -> {} ".format(self.data)


class Linked_list:
  def __init__(self):
    self.head = None
  
  def insert_at_start(self, data):
    node = Node(data)
    self.head = node
  
  def display(self):
    current = self.head
    while current != None:
      print(current)
      current = current.next

  def insert(self, pos, data):
    node = Node(data)
    current = self.head
    counter = 1
    while counter < pos:
      current = current.next
      counter += 1

    node.next = current.next
    current.next = node

  def reverse(self, segment):
    prev_node = None
    current = self.head
    next_node = None

    while current:
      next_node = current.next
      current.next = prev_node
      prev_node = current
      current = next_node
    self.head = prev_node

  def __sizeof__(self) -> int:
      counter = 0
      current = self.head
      while current:
        counter += 1
        current = current.next
      return counter

  def segmentation(self):
    segment_size = self.__sizeof__()
    self.reverse(segment_size)

train = Linked_list()
train.insert_at_start('umus')
train.insert(1, 'alone')
train.insert(2, 'lyi')
train.insert(3, 'fine')
train.insert(4, 'we')
train.reverse()