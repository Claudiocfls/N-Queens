from abc import ABC, abstractmethod 

class NQueensSolver(ABC):
    def __init__(self, numberOfQueens): 
        self.numberOfQueens = numberOfQueens
        self.solution = None
    
    def solve(self):
        pass
    
    def getSolution(self):
        return self.solution
    