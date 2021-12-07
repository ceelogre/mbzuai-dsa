''' 1. Create an iterator object for a number so we can print individual digits
Example: finish the class below so we can get the desired output.
'''
class Number:
  pass

my_number = Number(9603732)
my_number_iter = iter(my_number)
for number in my_number:
  print(number)

# should print 2 3 7 3 0 6 9

# finish the insert method found in linked_list.py. Then insert this node
# my_linked_list.insert(first, Node('middle'))