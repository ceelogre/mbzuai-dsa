class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def get_number(binary):
  current = binary
  str_bin = ''
  while current:
    str_bin += str(current.data)
    current = current.next
  return int(str_bin, 2)