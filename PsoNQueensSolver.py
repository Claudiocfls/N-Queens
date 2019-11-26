from NQueensSolver import NQueensSolver
from utils import fitness, generateRandomParticle, generateRandomVelocity, limitVelocity, limitPosition, generateRandomPosition, generateRandomSwap
import random
from DiscreteDimension import Position, Velocity

class Particle:
    def __init__(self, N):
        self.N = N
        self.position = Position()
        self.position.values = generateRandomPosition(N)
        self.velocity = Velocity()
        self.velocity.values = generateRandomSwap(N)
        self.pbest = (self.position, fitness(self.position.values))
        self.omega = 0.7
        self.alfa = 1.2
        self.beta = 2.3
    
    def update(self, gbest):
        self.r1 = random.uniform(0,1)
        self.r2 = random.uniform(0,1)
        
        inertiaFactor = self.omega*self.velocity
        cognitiveFactor = self.alfa*self.r1*(self.pbest[0] - self.position)
        socialFactor = self.beta*self.r2*(gbest - self.position)
        
        self.velocity = inertiaFactor + cognitiveFactor + socialFactor
        self.position = self.position + self.velocity

        if fitness(self.position.values) > self.pbest[1]:
            self.pbest = (self.position, fitness(self.position.values))

class PsoNQueensSolver(NQueensSolver):
    def __init__(self, numberOfQueens, chartGen = None):
        NQueensSolver.__init__(self, numberOfQueens)
        self.solution = None
        self.numberOfParticles = 10
        self.swarm = [Particle(numberOfQueens) for _ in range(self.numberOfParticles)]
        self.chartGen = chartGen
        self.iteration = 0

    def solve(self):
        gBestPosition = Position()
        gBestPosition.values = self.swarm[0].position.values
        gbest = (gBestPosition, self.swarm[0].pbest[1])
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
        
        self.solution = gbest[0].values
        print(gbest[1], self.iteration)
    
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
