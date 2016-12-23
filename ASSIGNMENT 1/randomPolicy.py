import blackjack
from pylab import *
from random import choice
 
def run(numEvaluationEpisodes):
    returnSum = 0.0
    for episodeNum in range(numEvaluationEpisodes):
        G = 0
        state = blackjack.init()
        while(state is not False):
            action = choice([0,1]) # pick action
# returns (reward, next state)
            result = blackjack.sample(state, action)
            G = G + result[0]
            state = result[1]            
        #print("Episode: ", episodeNum, "Return: ", G)
        returnSum = returnSum + G
    return returnSum / numEvaluationEpisodes
