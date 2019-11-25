from NQueensSolver import NQueensSolver
from utils import fitness

class PsoNQueensSolver(NQueensSolver):
    def __init__(self, numberOfQueens):
        NQueensSolver.__init__(self, numberOfQueens)
    
    def solve(self):
        pass
    
    def getSolution(self):
        return [2,4,6,8,3,1,7,5], fitness([2,4,6,8,3,1,7,5])
