class Number:
  def __init__(self, num) -> None:
      self.num = num
  
  def __iter__(self):
    return self
  
  def __next__(self):
    if self.num < 10:
      x = self.num
      self.num += 1
      return x
    else: raise StopIteration


my_number = Number(5)
my_number_iterator = iter(my_number)

for n in my_number_iterator:
  print(n)