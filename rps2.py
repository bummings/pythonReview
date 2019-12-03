import random

print('Rock, paper, scissors: ONE PLAYER\n\n')

# **** computer logic ****
rando = random.randint(0,2)

if rando == 0:
  computer = 'rock'
elif rando == 1:
  computer = 'paper'
else:
  computer = 'scissors'

# **** game logic ****
player1 = input('Your move: ')
print(f'Computer\'s move: {computer} \n')

# tie
if player1 == computer:
  print('It\'s a tie')

# variations on rock
elif player1 == 'rock':
  if computer == 'scissors':
    print('You win!')
  elif computer == 'paper':
    print('You lose.')

# variations on paper
elif player1 == 'paper':
  if computer == 'rock':
    print('You win!')
  elif computer == 'scissors':
    print('You lose.')

# variations on scissors
elif player1 == 'scissors':
  if computer == 'paper':
    print('You win!')
  elif computer == 'rock':
    print('You lose.')

# whoops
else:
  print('something ain\'t right')