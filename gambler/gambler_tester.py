# gambler tester
import random
import matplotlib.pyplot as plt
import math

p = float(input('chance of doubling money (p > 0.9 works best": ')) 
initMoney = 100
hedge = float(input('proportion of money saved: '))
rounds = int(input('rounds: '))

money1 = initMoney
money2 = initMoney
money1list = [math.log(money1)]
money2list = [math.log(money2)]
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
    money1list.append(math.log(money1,10))
    money2list.append(math.log(money2,10))

label2 = 'hedge ' + str(hedge)
plotTitle = 'balances for p = ' + str(p) + ' and hedge = ' + str(hedge)
plt.plot(xaxis, money1list, label='no hedge')
plt.plot(xaxis, money2list, label=label2)
plt.xlabel('Round')
plt.ylabel('log Balance')
plt.title(plotTitle)
plt.legend()
plt.show()
