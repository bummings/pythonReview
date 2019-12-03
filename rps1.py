import random
rando = random.randint(0,10)
print(rando)


print('rock paper scissors, two players')

player1 = input('player one: ')
player2 = input('player two: ')


# tie
if player1 == player2:
  print('it\'s a tie')

# variations on rock
elif player1 == 'rock':
  if player2 == 'scissors':
    print('player one wins')
  elif player2 == 'paper':
    print('player two wins')

# variations on paper
elif player1 == 'paper':
  if player2 == 'rock':
    print('player one wins')
  elif player2 == 'scissors':
    print('player two wins')

# variations on scissors
elif player1 == 'scissors':
  if player2 == 'paper':
    print('player one wins')
  elif player2 == 'rock':
    print('player two wins')

# whoops
else:
  print('something ain\'t right')