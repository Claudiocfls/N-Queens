from itertools import combinations
import random

# Receive a state and return the number
# of non-attacking pairs of queens
def fitness(state):
    indexes = [c for c in range(len(state))]
    pairs = list(combinations(indexes,2))
    
    def isNonAttackingPair(pair):
        i,j = pair
        if state[i] == state[j]:
            return False
        dcol = abs(i-j)
        drow = abs(state[i] - state[j])
        if dcol == drow:
            return False
        return True
    
    score = 0
    for pair in pairs:
        score = score + 1 if isNonAttackingPair(pair) else score

    return score

# Return a list with random numbers
# between 1 and 8 inclusive representing
# a particle on PSO algorithm
# IMPORTANT: PSO doesnt use this function
def generateRandomParticle(N):
    particle = []
    for i in range(N):
        randomPosition = random.randint(1,N)
        particle.append(randomPosition)
    
    return particle

def generateRandomGenome(N):
    return generateRandomParticle(N)

def generateRandomPosition(N):
    l = [c+1 for c in range(N)]
    position = []
    for j in range(N):
        indexChosen = random.randint(0,len(l)-1)
        position.append(l[indexChosen])
        del l[indexChosen]
    return position

def generateRandomSwap(N):
    numOfSwaps = random.randint(1,N//2)
    swaps = []
    for _ in range(numOfSwaps):
        i = random.randint(0,N-1)
        j = random.randint(0,N-1)
        swaps.append((i,j))
    return swaps

# Return a list with random numbers
# between -7 and 7 inclusive representing
# a velocity on PSO algorithm
# IMPORTANT: PSO doesnt use this function
def generateRandomVelocity(N):
    velocity = []
    for i in range(N):
        randomVelocity = random.randint(-7,7)
        velocity.append(randomVelocity)
    
    return velocity

# IMPORTANT: PSO doesnt use this function
def limitVelocity(v):
    v = max(-7,v)
    v = min(v,7)
    return v

# IMPORTANT: PSO doesnt use this function
def limitPosition(p):
    p = max(1,p)
    p = min(8,p)
    return p

