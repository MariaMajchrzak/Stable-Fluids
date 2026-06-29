import numpy as np


class FluidSolver:
    def __init__(self, size):
        self.velocity = np.zeros((size+2, size+2))
        self.density = np.zeros((size+2, size+2))
        self.size = size

    def step(self, dt, source):
        self.add_source(dt, source)
        self.diffuse(dt,0.001)

    def get_density(self):
        return self.density

    def add_source(self, dt, source):
        self.density += source *dt

    def diffuse(self, dt, diff):
        old_density = np.copy(self.density)
        for i in range(1,self.size+1,1):
            for j in range(1,self.size+1,1):
                laplacian = old_density[i, j-1] + old_density[i, j+1] + old_density[i-1, j] +  old_density[i+1,j] - 4 * old_density[i, j]
                self.density[i, j] = old_density[i,j] + laplacian * (diff * self.size *  self.size)* dt
