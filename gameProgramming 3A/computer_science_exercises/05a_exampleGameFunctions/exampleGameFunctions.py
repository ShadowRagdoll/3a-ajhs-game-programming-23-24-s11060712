# Example Game Functions, Gavin Kloeckner, v0.1.3
import random

damageNum = 0
moveSpeed = 0
armorStat = 0 # I don't think you need a health and an armor stat
baseHealth = 0 # try to make things as simple as possible
cardAmount = 0
cardType = 'Infantry Artillery Tank Aerial'.split() # how would this card type effect everything
teamSelect = ['Team 1', 'Team 2', 'Team 3', 'Team 4']


def getTeam():
    print('Welcome to the Intergelactic Card Game!\n')
    team = input(f'Before we get started, please input the Number of the team you would like to be on:\n{teamSelect}\n')
    while True:
        if team not in '1234':
            team = input('Team number not in range. Please input a number within 1-4 and press enter.\n') # this doesn't properly loop back
        elif team in '12345': # 5?
            clarify = input(f'Are you sure you want to be on team {team}?\n')
        if clarify == 'yes':
            print('Alright, now that you have selected your team,\nlet\'s move on.')
            break
        else:
            team = input(f'Please select what team you want to be on:\n{teamSelect}\n') 

getTeam() # why did you comment out the part below?

# def cardStatus(cardType, cardAmount):
#     while len(cardAmount) < 10:
#         cardType = cardType[random.randint(0,4)]
#         damageNum = damageNum[random.randint(0,50)]
#         moveSpeed = moveSpeed[random.randint(0,50)]
#         armorStat = armorStat[random.randint(0,10)]
#         baseHealth = baseHealth[random.randint(0,100)]
#         deck = cardType + " " + damageNum + " " + moveSpeed + " " + armorStat + " " + baseHealth
#         cardType += deck
#         cardAmount.append(deck)

# cardStatus(cardType, cardAmount)


# Code Review by Lily King