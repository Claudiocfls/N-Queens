from PsoNQueensSolver import PsoNQueensSolver
from DifferentialEvolutionSolver import DifferentialEvolutionSolver
from ChartGen import AnimatedChart
from utils import fitness

chart = AnimatedChart(60,28)
algo = PsoNQueensSolver(8, chart)
# algo = DifferentialEvolutionSolver(8, chart)
algo.solve()
chart.save()
sol = algo.getSolution()
print(sol)
print(fitness(sol))

