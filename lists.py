# Arrays

fruits = ['Apple', 'Banana', 'Cherries', 'Grapes']

print('Original List:', fruits)

fruits.append('Lemon')
print('Append:', fruits)

fruits.insert(1, 'Apricot')
print('Insert:', fruits)

print('List length:', len(fruits))

del(fruits[0])
print('Delete:', fruits)

print('Lemon is at index:', fruits.index('Lemon'))
