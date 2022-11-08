import random
import time
from MgsEnv import *

print('')
userName = input("Your username: ")
print('')
print(str(userName) + '! WELCOME ON THE "Miner Game Simulator"!!!')

while gameRunning == True:
    print('')
    print('SELECT A OPTION (1-3)')
    print('---' * 7)
    print('')
    print('1. Start A Game')
    print('2. Game Settings')
    print('3. Leave The Game')
    print('')
    runningSelect = input("Selected Option (1-3): ")
    print('')

    if runningSelect == '1':
        gameStart = True
        while gameStart == True:
            print('')
            print('SELECT A OPTION (1-4)')
            print('---' * 7)
            print('')
            print('1. Enter The Mine')
            print('2. Player Upgrades')
            print('3. Player Informations')
            print('4. Back To Menu')
            print('')
            startSelect = input("Select Option (1-4): ")
            print('')

            if startSelect == '1':
                mineStart = True
                while mineStart == True:
                    print('')
                    print('SELECT A OPTION (1-3)')
                    print('---' * 7)
                    print('')
                    print('1. Dig A Ores (10seconds)')
                    print('2. Select Your Mine Level')
                    print('3. Return')
                    print('')
                    mineStartSelect = input("Select Option (1-3): ")
                    print('')

                    if mineStartSelect == '1':
                        while miningTime != miningLeftTime:
                            print('')
                            oresGetted = random.randint(1,3)
                            ores = ores + oresGetted
                            print('Getted A: ' + str(oresGetted) + ' Ores. You have: ' + str(ores) + ' ores.')
                            miningTime = miningTime + 1
                            time.sleep(1)

                    elif mineStartSelect == '2':
                        print('COMMING SOON...')

                    elif mineStartSelect == '3':
                        mineStart = False
                    
                    else:
                        print('Select number of 1-3!!!')
            
            elif startSelect == '2':
                print('')
                print('COMMING SOON...')
                print('')

            elif startSelect == '3':
                print('')
                print(' PLAYER INFORMATIONS')
                print('---' * 7)
                print('Name:     ' + str(userName))
                print('Level:    ' + 'COMMING SOON...')
                print('Energy:   ' + 'COMMING SOON...')
                print('---' * 7)
                print('Ores:     ' + str(ores))
                print('Mine Lvl: ' + 'COMMING SOON...')
                print('---' * 7)
                print('')
            
            elif startSelect == '4':
                gameStart = False

            else:
                print('Select number of 1-4!!!')

    elif runningSelect == '2':
        print('Settings are comming soon...')

    elif runningSelect == '3':
        gameRunning = False

    else:
        print('Select number of 1-3!!!')