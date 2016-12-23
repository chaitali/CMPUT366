import blackjack
import numpy
import random
from pylab import *
from random import choice
from random import uniform

#alpha = 0.001
#eps = 0.01
gamma = 1



Q1 = 0.00001*rand(181,2)
Q2 = 0.00001*rand(181,2)

def policy(s):
    return argmax(Q1[s, :] + Q2[s, :])   
    

def learn(alpha, eps, numTrainingEpisodes):
    returnSum = 0.0
    for episodeNum in range(numTrainingEpisodes):
        G = 0
        s = blackjack.init()
        while(s is not False):
            
            x = uniform(0,1)
            if (x <= eps):
                action = choice([0,1])
            else: 
                action = policy(s)           
            
        
            # returns (reward, next state)
            result = blackjack.sample(s, action)
            ns = result[1]
            
            i = uniform(0,1)
            if (i > 0.5):
                Q1[s,action] = Q1[s,action] + alpha * (result[0] + gamma*(Q2[ns, argmax(Q1[ns,:])]) - Q1[s,action])
            else:
                Q2[s,action] = Q2[s,action] + alpha * (result[0] + gamma*(Q1[ns, argmax(Q2[ns,:])]) - Q2[s,action])
            # Fill in Q1 and Q2
            G = G + result[0]
            s = ns
        
        #print("Episode: ", episodeNum, "Return: ", G)
        returnSum = returnSum + G
        #if episodeNum % 10000 == 0 and episodeNum != 0:
        #    print("Average return so far: ", returnSum / episodeNum)

def evaluate(numEvaluationEpisodes):
    returnSum = 0.0
    for episodeNum in range(numEvaluationEpisodes):
        G = 0
        s = blackjack.init()
        while(s is not False):
            action = policy(s) 
            result = blackjack.sample(s, action)
            G = G + result[0]
            s = result[1]            
        # Use deterministic policy from Q1 and Q2 to run a number of
        # episodes without updates. Return average return of episodes.
        returnSum = returnSum + G
    return returnSum / numEvaluationEpisodes

#learn(alpha, eps, 10000000)
#print(evaluate(100000))
#blackjack.printPolicy(policy)
#blackjack.printPolicyToFile(policy)