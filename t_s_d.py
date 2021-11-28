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