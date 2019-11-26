import numpy as np
from matplotlib import pyplot as plt
from celluloid import Camera

class AnimatedChart:
    def __init__(self, yAxisMax, xAxisMax):
        self.yAxisMax = yAxisMax
        self.xAxisMax = xAxisMax
        self.camera = Camera(plt.figure())
        self.legends = [str(c) for c in range(self.xAxisMax)]
        self.y_pos = np.arange(self.xAxisMax)
    
    def addIteration(self, values, iteration):
        plt.bar(self.y_pos, values, align='center', alpha=0.5, color='b')
        plt.xticks(self.y_pos, self.legends)
        plt.title('Iteration {}'.format(iteration))
        plt.ylabel('# of particles')
        plt.xlabel('fitness function')
        self.camera.snap()

    def save(self):
        animation = self.camera.animate()  
        animation.save('iterations_pso.gif', writer="imagemagick")
