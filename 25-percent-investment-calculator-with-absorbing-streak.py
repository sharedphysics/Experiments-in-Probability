#!/usr/bin/env python3

import random

coin = ('success', 'failure', 'failure', 'failure' )
success, failure = 0, 0
rounds = 0
absorbingstreak = 0
bank = 100000000
print('***********************************************')
print('****   25% Investment Success Simulation   ****')
print('****                                       ****')
print('****       Starting with $100,000,000      ****')
print('***********************************************')
while True:
    flip = random.choice(coin)
    user_input = input('Press enter to invest $10 million, X to end the simulation:')
    if user_input == 'x' or user_input == 'X':
        percentagesuccess = round(success/rounds, 2)
        percentagefailure = round(failure/rounds,2)
        netinvestment = bank - 100000000
        totalgrowth = round(((bank/100000000-1)*100), 2)
        growthperperiod = round(((bank - 100000000)/rounds), 2)
        print(' ')
        print('**********************************')
        print('*****  Ending the Simulation *****')
        print('**********************************')
        print('  Rounds invested = {}'.format(rounds))
        print('  Orig = $100000000')
        print('  Bank = ${}'.format(bank))
        print('  Net Income = ${}'.format(netinvestment))
        print('  Total Growth = {}'.format(totalgrowth)+ '%')
        print('  Growth Per Round = ${}'.format(growthperperiod))
        print(' ')
        print('  Success = {}'.format(success))
        print('  Success Percentage = {}'.format(percentagesuccess) + '%')
        print('  Failure = {}'.format(failure))
        print('  Failure Percentage = {}'.format(percentagefailure) + '%')
        print(' ')
        break
    if bank <= 0:
        print(' ')
        print('**********************************')
        print('*********  BANKRUPTCY!!! *********')
        print('**********************************')
        print(' ')
        break
    if absorbingstreak == 4:
        rounds += 1
        failure += 1
        netinvestment = bank - 100000000
        percentagesuccess = round(success/rounds, 2)
        percentagefailure = round(failure/rounds,2)
        print(' ')
        print('*************************************************')
        print('  You have lost four times in a row. Game Over.')
        print('  Rounds invested = {}'.format(rounds))
        print('  Net income: ${}'.format(netinvestment))
        print(' ')
        print('  Success = {}'.format(success))
        print('  Success Percentage = {}'.format(percentagesuccess) + '%')
        print('  Failure = {}'.format(failure))
        print('  Failure Percentage = {}'.format(percentagefailure) + '%')
        print(' ')
        print('*************************************************')
        print(' ')
        break
    if bank <= 10000000:
        print(' ')
        print('**********************************')
        print('*****  Bank Balance is Low  ******')
        print('**********************************')
        print(' ')
    if flip == 'success':
        print(' ')
        print('** Successful investment. You earned $40,000,000 **'.
              format(flip))
        success += 1
        rounds += 1
        absorbingstreak = 0
        bank += 40000000
        print('  Bank = ${}'.format(bank))
        print('  Rounds invested = {}'.format(rounds))
    else:
        print(' ')
        print("** Failed investment. You lost $10,000,000 **".format(flip))
        failure += 1
        rounds += 1
        absorbingstreak += 1
        bank -= 10000000
        print('  Bank = ${}'.format(bank))
        print('  Rounds invested = {}'.format(rounds))