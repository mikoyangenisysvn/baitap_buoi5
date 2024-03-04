newTuple = ('a', 'b', 'c', 'd', 'e')
for i in newTuple:
  print(i)

for i in range(len(newTuple)):
  print(newTuple[i])

print('a' in newTuple)
print(newTuple.index('c'))


def seachTuple(p_tuple, element):
  for i in range(0, len(p_tuple)):
    if p_tuple[i] == element:
      return f"The {element} is  found at {i} index"
    return 'The elemetn is not found'
  print(seachTuple(newTuple, 'b'))
