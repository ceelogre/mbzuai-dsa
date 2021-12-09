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

  def delete(self, data):
    node_to_delete = self.search(data)
    if node_to_delete == None:
      return 'Unfound. Can\'t delete'
    current = self.head
    while current.next != node_to_delete:
      current = current.next
    current.next = node_to_delete.next

  def deleteEven(self):
    listHead = self.head
    while (listHead != None) and (listHead.data % 2 == 0):
        listHead = listHead.next
    if listHead == None:
        return listHead
    ans = Node(listHead.data)
    tmp = ans
    while listHead.next != None:
        listHead = listHead.next
        if listHead.data % 2 == 1:
            tmp.next = listHead
            tmp = tmp.next
    tmp.next = None
    return ans

train = Linked_list()
train.insert_at_start(1)
train.insert(1, 9)
train.insert(2, 3)
train.insert(3, 11)
train.insert(4, 5)
train.insert(5, 7)
new_head = (train.deleteEven())
train_ = Linked_list()
train_.head = new_head
train_.display()