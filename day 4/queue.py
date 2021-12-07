class Simple_queue:
  def __init__(self, max_size):
    self.queue = []
    self.max_size = max_size
  
  def enqueue(self, data):
    if not self.is_full():
      self.queue.append(data)
    else:
      print('Queue is full. Can\'t add item.')

  def print_queue(self):
    print(self.queue)

  def is_empty(self):
    return len(self.queue) == 0
  
  def dequeue(self):
    if self.is_empty():
      print('No items to remove')
      return None
    self.queue.pop(0)
  
  def peek(self):
    if self.is_empty():
      print('Can\'t peek. Queue empty')
      return None
    return self.queue[0]

  def is_full(self):
    return len(self.queue) == self.max_size

my_queue = Simple_queue(3)

my_queue.enqueue('second item')
my_queue.enqueue('first item')
my_queue.enqueue('third item')
my_queue.print_queue()

my_queue.dequeue()
my_queue.print_queue()

print(my_queue.peek())
my_queue.print_queue()

my_queue.dequeue()
my_queue.dequeue()
print(my_queue.peek())
my_queue.enqueue(1)
my_queue.enqueue(5)
my_queue.enqueue(10)
print(my_queue.is_full())

my_queue.enqueue('new item')
my_queue.print_queue()
print(my_queue.is_full())