#!/usr/bin/env python3

import random
coin = ('heads', 'tails')
heads, tails = 0, 0
games = 0
print('**********************************')
print('*****  Coin Flip Simulation  *****')
print('**********************************')
while True:
    flip = random.choice(coin)
    user_input = input('Press enter to flip, X to end the simulation:')
    if user_input == 'x' or user_input == 'X':
        percentageHeads = heads/games
        percentageTails = tails/games
        print(' ')
        print('**********************************')
        print('*****  Ending the Simulation *****')
        print('**********************************')
        print('Games played = {}'.format(games))
        print('  Heads = {}'.format(heads))
        print('  Heads Percentage = {}'.format(percentageHeads) + '%')
        print('  Tails = {}'.format(tails))
        print('  Tails Percentage = {}'.format(percentageTails) + '%')
        print(' ')
        break
    if flip == 'heads':
        print('Heads +1'.
              format(flip))
        heads += 1
        games += 1
    else:
        print("Tails +1".format(flip))
        tails += 1
        games += 1
