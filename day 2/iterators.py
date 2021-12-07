# iterator objects implement __iter__ and __next__ methods

l = [3, 54,32, 'name']
l_iterator = iter(l)

#print(l_iterator)
#print(next(l_iterator))
#print(next(l_iterator))
#print(next(l_iterator))
#print(next(l_iterator))
#print(next(l_iterator))

string = 'this is a string'
s_iterator = iter(string)

for a in s_iterator:
  print(a)

number = 3940
number_iterator = iter(3940)