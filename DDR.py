import time
import random
import pandas as pd
import numpy as np

#Welcome to DnD Dice Roller V1!

print('Welcome to DnD Dice Roller V1!')
time.sleep(0.5)

while True:

    whar = input('What die would you like to roll? 1.3 2.6 3.8 4.10 5.12 6.20 7.100: ')
    if whar == '1':
        rolls = int(input('How many times would you like to roll the d3? '))
        print('Calculating...')
        time.sleep(1)

        for i in range(rolls):
            roll = random.randint(0, 3)
            print(roll)
            i+1

        rerun = input('Rerun? Y/N ')
        if rerun == 'Y':
            print('Rerunning...')
            time.sleep(0.5)
        elif rerun == 'N':
            break

    if whar == '2':

            rolls = int(input('How many times would you like to roll the d6? '))
            print('Calculating...')
            time.sleep(1)

            for i in range(rolls):
                roll = random.randint(0, 6)
                print(roll)
                i+1

            rerun = input('Rerun? Y/N ')
            if rerun == 'Y':
                print('Rerunning...')
                time.sleep(0.5)
            elif rerun == 'N':
                break

    if whar == '3':

            rolls = int(input('How many times would you like to roll the d8? '))
            print('Calculating...')
            time.sleep(1)

            for i in range(rolls):
                roll = random.randint(0, 8)
                print(roll)
                i+1

            rerun = input('Rerun? Y/N ')
            if rerun == 'Y':
                print('Rerunning...')
                time.sleep(0.5)
            elif rerun == 'N':
                break

    if whar == '4':

            rolls = int(input('How many times would you like to roll the d10? '))
            print('Calculating...')
            time.sleep(1)

            for i in range(rolls):
                roll = random.randint(0, 10)
                print(roll)
                i+1

            rerun = input('Rerun? Y/N ')
            if rerun == 'Y':
                print('Rerunning...')
                time.sleep(0.5)
            elif rerun == 'N':
                break

    if whar == '5':

            rolls = int(input('How many times would you like to roll the d12? '))
            print('Calculating...')
            time.sleep(1)

            for i in range(rolls):
                roll = random.randint(0, 12)
                print(roll)
                i+1

            rerun = input('Rerun? Y/N ')
            if rerun == 'Y':
                print('Rerunning...')
                time.sleep(0.5)
            elif rerun == 'N':
                break

    if whar == '6':

            rolls = int(input('How many times would you like to roll the d20? '))
            print('Calculating...')
            time.sleep(1)

            for i in range(rolls):
                roll = random.randint(0, 20)
                print(roll)
                i+1

            rerun = input('Rerun? Y/N ')
            if rerun == 'Y':
                print('Rerunning...')
                time.sleep(0.5)
            elif rerun == 'N':
                break

    if whar == '7':

            rolls = int(input('How many times would you like to roll the d100? '))
            print('Calculating...')
            time.sleep(1)

            for i in range(rolls):
                roll = random.randint(0, 100)
                print(roll)
                i+1

            rerun = input('Rerun? Y/N ')
            if rerun == 'Y':
                print('Rerunning...')
                time.sleep(0.5)
            elif rerun == 'N':
                print('Thank you for using the DnD Dice Roller V1!')
                time.sleep(0.5)
                break