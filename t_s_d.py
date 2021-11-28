#tuples, sets and dictionaries
address = 'kk', 8, 'ave'
print(address[0])
print(address[1])
print(address[2])
#print(address[3])

#address[1] = 9

address = ()
print(address)
address = ('kk', )
print(address)

#x, y, z = address
#print(x, y, z)
address = 'kk', 8, 'ave'
x, y, z = address
print(x, y, z)
heights = (15, 27, 7, 28,15, 3)
print(heights)
heights = {15, 27, 7, 28,15, 3}
print(heights)

a = set('la flamme')
b = set('prague')
print(a)
print(a -b )
print(a|b)
print(a&b)
print(a^b)

id = {'Diane': 21, 'university': 'MBZUAI', 'weight': 128, 101: 'Data structures'}
print(id)
heights = {}
print(type(heights))

print(list(id))

id['weight']=150
print(id)
del id[101]
print(id)

for k,v in id.items():
  print(k,v)

#examples:

#fibonacci series
def fib(target):
  a,b = 0, 1
  for i in range(target) :
    a,b = b, a+b
  return b
print('Fibonacci',  fib(5))
# find the first unique number in a sequence
def first_unique(seq):
  return list(set(seq))[0]

print(first_unique([3,9,19,9,34,1,3]))
#return all vowels and their respective counts from a string
def get_vowels(string):
  results = dict()
  for letter in 'aieou':
    if letter in string:
      occ = string.count(letter)
      results[letter] = occ
  return results

print(get_vowels('abracadabra'))

# given a dictionary containing the names and ages of a group of people, return the name of the oldest person

def oldest(people):
  ages = sorted([ age for name,age in people.items()])[-1]
  return ages
print(oldest(dict(Emma= 71, Jack= 45, Amy= 15,  Ben= 29)))