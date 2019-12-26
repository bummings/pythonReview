# let's create a new list
demo = ['apples', 'kiwi', 'watermelon']

#list methods:

total = len(demo) # length of said list
print(demo)
print (total)

r = range(1, 5)
rangeDemo = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']


friends = ['faux', 'graf', 'kno']
print(friends)
print('faux' in friends) # boolean repsponse for list item

colors = ['red', 'green', 'blue', 'cyan', 'magenta', 'yellow', 'key']

# you can get real clever with these, bruh
if 'cyan' in colors:
  print('$$$$$$$$$$$$$$')
else:
  print('NOPE')

# colorSubmission = input('Which color are you looking for? ')

# if colorSubmission in colors:
#   print('Yes, we have that color')
# else:
#   print(f'Are you kidding me? What kind of color is ' + colorSubmission)

for color in colors:  # iterate over an entire list
  print(color)



index = 0
while index < len(colors):
  print(f'{index}: {colors[index]}')
  index += 1

# LIST METHODS
listMethods = ['a','b','c']

print('\n')       # appending to a list 
print(f'List prior to APPEND: {listMethods}')
listMethods.append('d')
print(f'List post APPEND: {listMethods}')



print('\n')     # extending multiple to a list 
print(f'List prior to EXTEND: {listMethods}')
listMethods.extend(['e','f'])
print(f'List post EXTEND: {listMethods}')

print('\n')           # inserting into a list
print(f'List prior to INSERT: {listMethods} ')
listMethods.insert(2, 'INSERTED')
listMethods.insert(len(listMethods), 'FINAL')
print(f'List post INSERT: {listMethods}')

print('\n')         # pop that last one (FINAL)
print(f'List prior to POP: {listMethods}')
listMethods.pop()
print(f'List post POP: {listMethods}')


