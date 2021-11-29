#tuples, sets and dictionaries
address = 'kk', 8, 'ave'
#print(address[0])
#print(address[1])
#print(address[2])
#print(address[3])

#address[1] = 9
empty_tuple = ()
#print(type(empty_tuple))

one_tuple = ('age',)
#print(one_tuple)

t = (1,'2',3, 'another string')
#print(t)
#print(address)

add_1, add_2, add_3 = address
#print(add_1)
#print(add_3)

#add_1, add_2 = address

## create a set
heights = {15, 9, 8,4}
heights_ = {15, 9, 9, 3}
heights_.add(15)
#print(heights_)
#print(heights - heights_)
#print(heights ^ heights_)
#print(heights & heights_)

id = {'Diane': 21, 'university': 'MBZUAI', 'weight': 128, 101: 'Data structures'}

id['Diane'] = 31
#print(id['Diane'])

del id[101]
#print(id)

id['height'] = 16.8
#print(id)

#print(3 in id)
#print('university' in id)

for k,v in id.items():
  #print(k,v)

  #examples:

  #fibonacci series
  def fib(nth_number):
    a, b= 0, 1
    for i in range(nth_number):
      a, b = b, a+b
    return b

#print(fib(4))
#print(fib(40))

#find the first unique number in a given sequence
#find_unique([3,9,19,6,3,5]) => 9
def find_unique(l):
  # loop through all items
  # check if a given item does not exist in the remaining array and break
  for i in range(len(l)):
    if l[i] not in l[i+1:] and l[i] not in l[:i]:
      y = l[i]
      break
  return y

#print(find_unique([3,9,19,6,3,5]))
#print(find_unique([4, 2,6, 9, 10, 6, 2, 4, 9, 10, 11]))
# return all vowels and their respective counts in a given string
# get_vowels_count('fox') => {'o': 1}
# get_vowels_count('abracadabra') => {'a': 5}
# get_vowels_count('aerial') => {'a': 2, 'e': 1, 'i': 1}
def get_vowels_count(string):
  # declare an empty dictionary
  # loop through the string
  # if the given vowel is not in the dictionary, add it as key and value as 1
  # else, increase its value by 1
  # return the dictionary

  results = dict()
  vowels = 'aiuoe'

  for letter in string:
    if letter in vowels:
      if letter not in results:
        results[letter] = 1
      else: results[letter] += 1
  return results

##print(get_vowels_count('fox'))
##print(get_vowels_count('abracadabra'))
##print(get_vowels_count('aerial'))

#Given a dictionary containing names and ages of a group of people, return the name of the oldest person
# oldest({'Patrick': 24, 'Solange': 49, 'Brian': 93, 'Gael': 15}) => 'Brian'

def oldest(people):
  # return the maximum of values
  max_val =  max(people.values())
  return next(k for k,v in people.items() if v == max_val)

def oldest_(people):
  # declare max as zero
  # loop through the dictionary
  # compare value and max
  # if greater, value is the new max
  # assign key to the name
  # return the name
  pass
print(oldest({'Patrick': 24, 'Solange': 49, 'Brian': 93, 'Gael': 15}))
