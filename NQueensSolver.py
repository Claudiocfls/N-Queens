from abc import ABC, abstractmethod 
from utils import fitness

class NQueensSolver(ABC):
    def __init__(self, numberOfQueens): 
        self.numberOfQueens = numberOfQueens
        self.solution = None
        self.fitnessOfSolution = None
        self.iteration = None
    
    def solve(self):
        pass
    
    def getSolution(self):
        return self.solution, fitness(self.solution), self.iteration

    