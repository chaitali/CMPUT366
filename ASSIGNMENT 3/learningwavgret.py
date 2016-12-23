import mountaincar
from Tilecoder import numTilings, numTiles, tilecode
from pylab import *  # includes numpy

numRuns = 5
n = numTiles * 3

def learn(alpha=0.1 / numTilings, epsilon=0.0, numEpisodes=200):
    theta1 = -0.001 * rand(n)
    theta2 = -0.001 * rand(n)
    returnSum = 0.0
    
    for episodeNum in range(numEpisodes):
        G = 0.0
        s = mountaincar.init()
        step = 0
        while(s != None):
            step += 1
            F = [0] * numTilings  
            tilecode(s[0], s[1], F) 
            
            Q = Qs(F, np.add(theta1, theta2)/2)
            
            # choose action
            x = uniform(0,1)
            if (x <= epsilon):
                a = choice([0,1,2])
            else: 
                a = np.argmax(Q)            
            
            # next state 
            r, ns = mountaincar.sample(s, a)
            G += r  
            
            # choose a theta
            x = uniform(0,1)
            if(x > 0.5):
                theta = theta1
                next_theta = theta2
            else:
                theta = theta2
                next_theta = theta1
            
            
                
            if (ns == None):             
                for i in F:
                    theta[i + (a * numTiles)] += alpha * (r - Qval(a, F, theta))
                break
            
            nF = [0] * numTilings
            tilecode(ns[0], ns[1], nF)
            nQ = Qs(nF, theta)
            na = argmax(nQ) 
            for i in F:
                theta[i + (a * numTiles)] += alpha * (r + Qval(na,nF,next_theta) - Qval(a, F, theta))
            s = ns
                
            
       
        print("Episode:", episodeNum, "Steps:", step, "Return: ", G)
       
        returnSum += G
        if(episodeNum != 0):
            
            avg = returnSum/episodeNum
            writeX(avg, episodeNum)        
    print("Average return:", returnSum / numEpisodes)
    #avg = returnSum / numEpisodes
    
    return returnSum, theta1, theta2

def Qval(a, F, theta):
    val = 0
    for i in F:
        val += theta[i + (a * numTiles)]
    return val    
    


#Additional code here to write average performance data to files for plotting...
#You will first need to add an array in which to collect the data
def writeX(averageRet, episodeNum):
    
    
    fout.write(str(episodeNum) + ' ' + str(averageRet))
    fout.write("\n")
    
    




def writeF(theta1, theta2):
    fout = open('value', 'w')
    steps = 50
    for i in range(steps):
        for j in range(steps):
            F = [-1] * numTilings
            tilecode(-1.2 + (i * 1.7 / steps), -0.07 + (j * 0.14 / steps), F)
            height = -max(Qs(F, theta1 + theta2 / 2))
            fout.write(repr(height) + ' ')
        fout.write('\n')
    fout.close()
    
def Qs(tileIndices, theta):
    
    Q = zeros(3)  
    for action in range(3):
        for i in tileIndices:
            Q[action] += theta[i + (action*numTiles)]
    return Q
    

if __name__ == '__main__':
    runSum = 0.0
    fout = open('avgret.dat','w')
    for run in range(numRuns):
        returnSum, theta1, theta2 = learn()
        writeF(theta1, theta2)
        runSum += returnSum
    fout.close()
    print("Overall performance: Average sum of return per run:", end="")
    print(runSum / numRuns)
