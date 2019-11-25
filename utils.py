from itertools import combinations

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

