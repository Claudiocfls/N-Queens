from NQueensSolver import NQueensSolver
from utils import fitness, generateRandomParticle, generateRandomVelocity

class Particle:
    def __init__(self, N):
        self.N = N
        self.positions = generateRandomParticle(N)
        self.velocities = generateRandomVelocity(N)
        self.pbest = (self.positions[:], fitness(self.positions))
        self.omega = 1
        self.beta = 1
        self.alfa = 1
    
    def update(self, gbest):
        for i in range(self.N):
            self.velocities[i] = self.omega*self.velocities[i] + self.alfa*(self.pbest[0][i] - self.positions[i]) + self.beta*(gbest[i] - self.positions[i])
            self.positions[i] = self.positions[i] + self.velocities[i]
            self.positions[i] = min(8, self.positions[i])
            self.positions[i] = max(1, self.positions[i])
        
        if fitness(self.positions) > self.pbest[1]:
            self.pbest = (self.positions[:], fitness(self.positions))
        else:
            self.positions = self.pbest[0][:]


class PsoNQueensSolver(NQueensSolver):
    def __init__(self, numberOfQueens):
        NQueensSolver.__init__(self, numberOfQueens)
        self.solution = None
        self.numberOfParticles = 20
        self.swarm = [Particle(numberOfQueens) for _ in range(self.numberOfParticles)]

    def solve(self):
        gbest = (self.swarm[0].positions, self.swarm[0].pbest[1])
        gbest = self.updateGBest(gbest)

        i = 0
        while i < 1000:
            i += 1
            for p in self.swarm:
                p.update(gbest[0])
            gbest = self.updateGBest(gbest)
        
        self.solution = gbest[0]
        print(gbest[1])
    
    def updateGBest(self, gbestValue):
        gbest = gbestValue
        for p in self.swarm:
            if p.pbest[1] > gbest[1]:
                gbest = (p.pbest[0],p.pbest[1])
        
        return gbest
