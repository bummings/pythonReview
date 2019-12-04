# AY- remember you can `mv fileToRename fileNewName` in UNIX, lol

# for letter in 'bruh':
#   print(letter)

# for number in range(1,6):
#   print(number)

# ranges: if ya just wanna  print numbers

# range(7) gives ya integers from 0 thru 6
# range(1,8) gives ya intergers from 1 thru 7
# range(1,10,2) gives ya odds from 1 thru 10 (skippin 2)
# range(7,0,-1) counts down by 1, 7 to 0

# nums = range(1,10,2)

# for x in nums:
#   print(x)

# nums = input('how many times i gotta tell ya to? ')
# nums = int(nums)

# for times in range(0, nums):
#   print('do dat!')

# Loop thru the numbers 1-20
#   for 4 and 13, print "X is REALLY BAD"
#   for even numbers print "X is even"
#   for odd numbers print "X is odd"

nums = range(1,21)

# for num in nums:
#   if num == 4 or num == 13:
#     print(f'{num} is REALLY BAD')
#   elif num % 2 == 0:
#     print(f'{num} is even')
#   elif num % 2 != 0:
#     print(f'{num} is odd')
#   else:
#     print(num)


for num in nums:
  if num == 4 or num == 13:
    state = "REALLY BAD"
  elif num % 2 == 0:
    state = 'even'
  else:
    state = 'odd'
  print(f'{num} is {state}')