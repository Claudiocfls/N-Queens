from NQueensSolver import NQueensSolver
from utils import fitness, generateRandomParticle, generateRandomVelocity
import random

class Particle:
    def __init__(self, N):
        self.N = N
        self.positions = generateRandomParticle(N)
        self.velocities = generateRandomVelocity(N)
        self.pbest = (self.positions[:], fitness(self.positions))
        self.omega = 0.8
        self.alfa = 1.8
        self.beta = 2.5
    
    def update(self, gbest):
        r1 = random.uniform(0,1)
        r2 = random.uniform(0,1)
        for i in range(self.N):
            self.velocities[i] = round(self.omega*self.velocities[i] + self.alfa*r1*(self.pbest[0][i] - self.positions[i]) + self.beta*r2*(gbest[i] - self.positions[i]))
            self.positions[i] = self.positions[i] + self.velocities[i]
            self.positions[i] = min(8, self.positions[i])
            self.positions[i] = max(1, self.positions[i])
        
        if fitness(self.positions) > self.pbest[1]:
            self.pbest = (self.positions[:], fitness(self.positions))

class PsoNQueensSolver(NQueensSolver):
    def __init__(self, numberOfQueens, chartGen = None):
        NQueensSolver.__init__(self, numberOfQueens)
        self.solution = None
        self.numberOfParticles = 50
        self.swarm = [Particle(numberOfQueens) for _ in range(self.numberOfParticles)]
        self.chartGen = chartGen
        self.iteration = 0

    def solve(self):
        gbest = (self.swarm[0].positions, self.swarm[0].pbest[1])
        gbest = self.updateGBest(gbest)

        i = 0
        while i < 1000:
            self.iteration += 1
            i += 1
            for p in self.swarm:
                p.update(gbest[0])
            gbest = self.updateGBest(gbest)
            if self.chartGen and self.iteration % 10 == 0:
                self.generateValuesToChart()
        
        self.solution = gbest[0]
        print(gbest[1])
    
    def generateValuesToChart(self):
        values = [0]*28
        for p in self.swarm:
            v = p.pbest[1]
            values[v-1] += 1
        self.chartGen.addIteration(values, self.iteration)
    
    def updateGBest(self, gbestValue):
        gbest = gbestValue
        for p in self.swarm:
            if p.pbest[1] > gbest[1]:
                gbest = (p.pbest[0],p.pbest[1])
        
        return gbest
