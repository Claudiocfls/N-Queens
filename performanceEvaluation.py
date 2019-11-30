from PsoNQueensSolver import PsoNQueensSolver
from DifferentialEvolutionSolver import DifferentialEvolutionSolver
from ChartGen import BarChart
from utils import fitness

numberOfSamples = 10
x = []
y = []
for numberOfQueens in range(8,12):
    acc = 0
    for i in range(numberOfSamples):
        algo = PsoNQueensSolver(numberOfQueens)
        algo.solve()
        sol = algo.getSolution()
        acc += sol[-1]
    average = acc / numberOfSamples
    x.append(numberOfQueens)
    y.append(average)

print(x,y)
chart = BarChart(x,y)
chart.show()

