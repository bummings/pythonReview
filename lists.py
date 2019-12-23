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

colorSubmission = input('Which color are you looking for?')

if colorSubmission in colors:
  print('Yes, we have that color')
else:
  print(f'Are you kidding me? What kind of color is ' + colorSubmission)
