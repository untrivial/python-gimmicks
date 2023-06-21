# Linked List Implementation
# 12/17/2022

import csv
import hashlib

chain = []
data = []

def printChain():
    for block in chain:
        print(block)


def addRootBlock(blockData):
    data = []
    data.append(0)
    data.append(blockData)
    data.append(hashlib.sha256(str(str(0) + blockData).encode('utf-8')).digest())
    chain.append(data)


def addBlock(blockData):
    data = []
    data.append(len(chain))
    data.append(blockData)
    data.append(hashlib.sha256(str(str(len(chain)) + blockData + str(chain[len(chain)-1][2])).encode('utf-8')).digest())
    chain.append(data)


def editBlock(blockId, newBlockData):
    chain[blockId][1] = newBlockData
    for w in range(blockId, len(chain)):
        if blockId != 0:
            chain[w][2] = hashlib.sha256(str(str(w) + str(chain[w][1]) + str(chain[blockId-1][2])).encode('utf-8')).digest()
        else:
            chain[0][2] = hashlib.sha256(str(str(0) + str(chain[0][1])).encode('utf-8').digest())
