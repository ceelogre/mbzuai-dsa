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
    while first_variable.head != None:
      first_variable.head = first_variable.head.next
    first_variable.head = new_node
  def insert():
    pass
  
  def traverse(first_variable):
    while first_variable.head != None:
      print(first_variable.head.data)
      first_variable.head = first_variable.head.next

my_linked_list = Linked_list()
my_linked_list.insert_at_start(first)
my_linked_list.traverse()

last = Node('last')
my_linked_list.insert_at_end(last)
my_linked_list.traverse()