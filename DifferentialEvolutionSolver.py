from NQueensSolver import NQueensSolver
from utils import fitness, generateRandomGenome
import random

class DifferentialEvolutionSolver(NQueensSolver):
    def __init__(self, numberOfQueens, chartGen = None):
        NQueensSolver.__init__(self, numberOfQueens)
        # Constants 
        self.numberOfGenomes = 50
        self.scaleFactor = 0.6
        self.crossOverConstant = 0.5
        # Other variables
        self.solution = [0]*numberOfQueens
        self.genomes = [generateRandomGenome(numberOfQueens) for _ in range(self.numberOfGenomes)]
        self.chartGen = chartGen
        self.iteration = 0

    def solve(self):

        maxIteration = 1000
        for _ in range(maxIteration):
            self.iteration += 1
            for g_ind in range(len(self.genomes)):
                g = self.genomes[g_ind]
                g1 = self.genomes[random.randint(0,self.numberOfGenomes-1)]
                g2 = self.genomes[random.randint(0,self.numberOfGenomes-1)]
                g3 = self.genomes[random.randint(0,self.numberOfGenomes-1)]
                donor = self.generateDonor(g1, g2, g3)
                trial = self.generateTrial(g, donor)
                
                if fitness(g) < fitness(trial):
                    self.genomes[g_ind] = trial
                    if fitness(self.solution) < fitness(trial):
                        self.solution = trial

            if self.chartGen and self.iteration % 10 == 0:
                self.generateValuesToChart()
    
    def generateValuesToChart(self):
        values = [0]*28
        for g in self.genomes:
            v = fitness(g)
            values[v-1] += 1
        self.chartGen.addIteration(values, self.iteration)

    def generateDonor(self, g1, g2, g3):
        donor = []
        for i in range(len(g1)):
            new_value = g1[i] + self.scaleFactor * (g2[i] - g3[i])
            new_value = int(new_value + 0.5)
            new_value = min(new_value, 8)
            new_value = max(new_value, 0)
            donor.append(new_value)
        return donor
    
    def generateTrial(self, g, donor):
        trial = []
        for i in range(len(g)):
            if random.uniform(0,1) < self.crossOverConstant:
                trial.append(donor[i])
            else:
                trial.append(g[i])
        return trial

    