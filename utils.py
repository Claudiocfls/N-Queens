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
def generateRandomParticle(N):
    particle = []
    for i in range(N):
        randomPosition = random.randint(1,8)
        particle.append(randomPosition)
    
    return particle

def generateRandomGenome(N):
    return generateRandomParticle(N)

# Return a list with random numbers
# between -7 and 7 inclusive representing
# a velocity on PSO algorithm
def generateRandomVelocity(N):
    velocity = []
    for i in range(N):
        randomVelocity = random.randint(-7,7)
        velocity.append(randomVelocity)
    
    return velocity

def limitVelocity(v):
    v = max(-7,v)
    v = min(v,7)
    return v

def limitPosition(p):
    p = max(1,p)
    p = min(8,p)
    return p

