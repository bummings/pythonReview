print('rock paper scissors, yo')

print('player one: ')
player_1_choice = input()

print('player two: ')
player_2_choice = input()

#variations on rock
if player_1_choice == 'rock' and player_2_choice == 'scissors':
  print('player one: rock  |  player two: scissors')
  print('player one wins')
elif player_1_choice == 'rock' and player_2_choice == 'paper':
  print('player one: rock  |  player two: paper')
  print('player two wins')
elif player_1_choice == 'rock' and player_2_choice == 'rock':
  print('player one: rock  |  player two: rock')
  print('it\'s a tie')

#variations on paper
elif player_1_choice == 'paper' and player_2_choice == 'rock':
  print('player one: paper  |  player two: rock')
  print('player one wins')
elif player_1_choice == 'paper' and player_2_choice == 'scissors':
  print('player one: paper  |  player two: scissors')
  print('player two wins')
elif player_1_choice == 'paper' and player_2_choice == 'paper':
  print('player one: paper  |  player two: paper')
  print('it\'s a tie')

#variations on scissors
elif player_1_choice == 'scissors' and player_2_choice == 'paper':
  print('player one: scissors  |  player two: paper')
  print('player one wins')
elif player_1_choice == 'scissors' and player_2_choice == 'rock':
  print('player one: scissors  |  player two: rock')
  print('player two wins')
elif player_1_choice == 'scissors' and player_2_choice == 'scissors':
  print('player one: scissors  |  player two: scissors')
  print('it\'s a tie')