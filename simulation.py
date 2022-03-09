import math
import random
#import numpy as np
#import matplotlib.pyplot as plt
#import matplotlib.pyplot as plt
#import numpy as np
# This is the simulation of upper Yahtzee
class Player:

    def __init__(self, score):
        # sheet from 0 to 5, track filling
        self.sheet = [-1,-1,-1,-1,-1,-1]
        self.score = score

    def add_score(self, update, num):
        if(self.sheet[num] != -1):
            return "error"
        self.score = self.score + update
        self.sheet[num] = update

    def get_score(self):
        return self.score

    def get_sheet(self):
        return self.sheet  

    def unfill_sheet(self,num):
        if self.sheet[num] == -1:
            return True
        else:
            return False


def most_frequent(List, filledList):
    #print(List)
    for num in filledList:
        #print(num)
        List = list(filter((num).__ne__, List))
    #print(List)
    if not List:
        return 0,0
    counter = 0

    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency > counter) or (curr_frequency == counter and i > num):
            counter = curr_frequency
            num = i
 
    return num, counter

def select(dices, unfilledList):
    freq = 0
    score = 0
    num = 1
    for i in unfilledList:
        if (i*dices.count(i) + dices.count(i) > score):
            num = i
            freq = dices.count(i)
            score = i*dices.count(i) + freq
    return num, freq

def selectTwo(dices, unfilledList):
    freq = 0
    score = 0
    num = 1
    for i in unfilledList:
        if (i*dices.count(i)  > score):
            num = i
            freq = dices.count(i)
            score = i*dices.count(i) 
    return num, freq



def playerOne(player):
    for i in range(0,5):
        dices[i] = random.randint(1,6)
    filledList = []
    for i in range(0,6):
        #print(players[nextPlayer].sheet)
        if players[player].unfill_sheet(i) == True:
            #print(i)
            filledList.append((i+1))
    num, freq = select(dices, filledList)
    for i in range(0,5):
        if num == 0:
            dices[i] = random.randint(1,6)
        elif dices[i] != num:
            dices[i] = random.randint(1,6)
    num, freq = select(dices, filledList)
    for i in range(0,5):
        if num == 0:
            dices[i] = random.randint(1,6)
        elif dices[i] != num:
            dices[i] = random.randint(1,6)
    num, freq = select(dices, filledList)
    #print(num, freq)
    countTwo = 0 
    players[player].add_score(num*freq,(num-1))




def playerTwo(player):
    for i in range(0,5):
        dices[i] = random.randint(1,6)
    filledList = []
    for i in range(0,6):
        #print(players[nextPlayer].sheet)
        if players[player].unfill_sheet(i) == True:
            #print(i)
            filledList.append((i+1))
    num, freq = select(dices, filledList)
    for i in range(0,5):
        if num == 0:
            dices[i] = random.randint(1,6)
        elif dices[i] != num:
            dices[i] = random.randint(1,6)
    num, freq = select(dices, filledList)
    for i in range(0,5):
        if num == 0:
            dices[i] = random.randint(1,6)
        elif dices[i] != num:
            dices[i] = random.randint(1,6)
    num, freq = select(dices, filledList)
    #print(num, freq)
    #players[currentPlayer].get_score()-players[nextPlayer].get_score()-num*freq
    #players[currentPlayer].get_sheet()[num-1]-expect[num-1] < 8
    #players[currentPlayer].get_sheet()[num-1]-num*freq < 8)
    if (players[currentPlayer].get_sheet()[num-1]-num*freq < 8):
        players[player].add_score(num*freq,(num-1))
    else:
        for i in range(0,1):
            if players[player].unfill_sheet(i):
                sumDiceTwo = 0
                for j in range(0,5):
                    if dices[j] == (i+1):
                        sumDiceTwo += dices[j]
                players[player].add_score(sumDiceTwo,i)
                break
        if players[player].unfill_sheet(i):
            players[player].add_score(num*freq,(num-1))


numberOfPlayers = 2 ## the number of players
numberOfGames = 10000
numberOfRound = 1
expect = [2.5408, 5.2932, 8.208, 10.8065, 13.4402, 15.6082]
HistData = [0]*numberOfRound
run = numberOfGames // 100
x = [[0]*100]*10
y = [[0]*100]*10
for i in range(10):
    for j in range(100):
        x[i][j] = j*100
    y[i] = [0]*100
rate = [0]*10
wins=[] # array to keep track of how many times each player wins
for i in range(numberOfPlayers):
	wins.append(0)
        
res = [0,0]
count = 0
allOne = []
allTwo = []
oneList = [0]*6
twoList = [0]*6
for run in range(numberOfRound):
    for game in range(numberOfGames): ## main game loop
        count += 1
        ### prepare the game
        players=[]
        for i in range(numberOfPlayers):
            players.append(1)

        for i in range (numberOfPlayers):
            players[i] = Player(0)

        currentPlayer = game % numberOfPlayers
        nextPlayer = (game+1) % numberOfPlayers
        round = 0

        while(round < 6):
            dices = [0,0,0,0,0]

            #user 1
            playerOne(currentPlayer)
            #user 2
            #gap = players[currentPlayer].get_score() - players[nextPlayer].get_score()
            playerTwo(nextPlayer)
            
            round = round + 1
        for i in range(0, 6):
            oneList[i] += players[currentPlayer].get_sheet()[i]
            twoList[i] += players[nextPlayer].get_sheet()[i]
        allOne.append(players[currentPlayer].get_score())
        allTwo.append(players[nextPlayer].get_score())
        meanOne = sum(allOne)/count
        meanTwo = sum(allTwo)/count
        #print(players[currentPlayer].get_score(), players[nextPlayer].get_score())
        if players[currentPlayer].get_score() > players[nextPlayer].get_score():
            res[0] += 1
        if players[currentPlayer].get_score() < players[nextPlayer].get_score():
            res[1] += 1
    HistData[run] = res[0]/numberOfGames
    print(res[0]/(res[0]+res[1]))
    res = [0,0]
    #if game % run == 0 and (game // run != 0):
    #    y[runs][game // run] = res[0]/(res[1]+res[0])
print(res[0]/numberOfGames)
result = [number / numberOfGames for number in oneList]
print(result)
#print(x)
#print(y)
#print(rate)
#for i in range(2):
#    plt.plot(x[i][2:], y[i][2:])
#plt.xlabel('x - axis')
# naming the y axis
#plt.ylabel('y - axis')
 
# giving a title to my graph
#plt.title('My first graph!')
#print(y[2:])
#print(res)
#plt.hist(HistData)
#plt.show()
#print(HistData)
print(meanOne)
print(meanTwo)