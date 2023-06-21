# gambler meta-tester
import random
import matplotlib.pyplot as plt
import math
import numpy as np

def results(p, hedge, rounds):
    money1 = 100
    money2 = 100

    counter = 1
    xaxis = [1]
    
    for i in range(rounds):
        counter += 1
        xaxis.append(counter)
        if random.random() < p:
            money1 *= 2
            money2 = hedge * money2 + (1 - hedge) * money2 * 2
        else:
            money1 = 1
            money2 = hedge * money2


    if money2 > money1:
        return [hedge, money2 - money1]
    else:
        return 'a'
        
    
output1 = []
output2 = []
outputStr = []
maxi = 0
maxi2 = 0
trials = 1000

increments = 100
for i in range(increments):
    p = 0.50 + i * (0.499 / increments)
    for j in range(increments):
        hedge = 0.01 + j * (0.989 /increments)
        foo1 = results(p, hedge, trials)
        if foo1 != 'a' and foo1[1] > maxi:
            maxi = foo1[1]
            maxi2 = foo1[0]
    if foo1 != 'a':
        output2.append(maxi2)
        output1.append(p)

for i in range(len(output1)):
    outputStr.append(output1[i]*-2 + 2)
        
#for i in range(len(output1)):
 #   print(output1[i], output2[i])
    
plotTitle = "Trials: " + str(trials)
plt.plot(output1, output2)
plt.plot(output1, outputStr)
plt.xlabel('p')
plt.ylabel('hedge')
plt.title(plotTitle)
plt.show()


