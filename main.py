from PsoNQueensSolver import PsoNQueensSolver
from ChartGen import AnimatedChart

chart = AnimatedChart(60,28)
algo = PsoNQueensSolver(8, chart)
algo.solve()
chart.save()
print(algo.getSolution())