class Node:
  def __init__(first_variable, data):
    first_variable.data = data
    first_variable.next = None
  

first = Node('first')
#print(first.data)
#print(first.next)

class Linked_list:
  def __init__(first_variable):
    first_variable.head = None

  def insert_at_start(first_variable, node):
    first_variable.head = node
  def insert_at_end(first_variable, new_node):
    current_node = first_variable.head
    while current_node.next != None:
      current_node = current_node.next
    current_node.next = new_node

  def insert(self, pos, newest_node):
    for i in range(2, pos):
      if self.head != None:
        self.head = self.head.next
    newest_node.next = self.head.next
    self.head.next = newest_node
    pass
  
  def traverse(first_variable):
    current_node = first_variable.head
    while current_node != None:
      print(current_node.data)
      current_node = current_node.next
    
  def search():
    pass

  def delete():
    pass

my_linked_list = Linked_list()
my_linked_list.insert_at_start(first)
my_linked_list.traverse()

last = Node('last')
my_linked_list.insert_at_end(last)
my_linked_list.traverse()

my_linked_list.insert(2, Node('middle'))
my_linked_list.traverse()