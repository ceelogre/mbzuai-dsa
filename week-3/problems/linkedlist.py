#sort a linked list
class Node:
  def __init__(self, data):
    self.data =  data
    self.next = None
  def __repr__(self):
    return 'Node data-> {0}, next -> {1}'.format(self.data, self.next)

class Singly_linkedlist:
  def __init__(self):
    self.head = None

  def insert(self, pos, data):
    node = Node(data)
    if self.head == None:
      self.head = node
      return
    counter = 0
    current = self.head

    while current != None:
      counter += 1
      if counter == pos:
        break
      current = current.next
      
    node.next = current.next
    current.next = node

  def display(self):
    current = self.head

    while current != None:
      print(current.data)
      current = current.next

  def sort(self):
    swapped = True
    while swapped:
      swapped = False
      current = self.head
      while current.next != None:
        if current.data > current.next.data:
          temp = current.data
          current.data = current.next.data
          current.next.data = temp
          swapped = True
        current = current.next


