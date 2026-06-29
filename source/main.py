import keyboard
import numpy as np
from Renderer import Renderer
from FluidSolver import  FluidSolver

SIZE =100

running = True
renderer = Renderer(SIZE)
fluidSolver = FluidSolver(SIZE)
source = np.zeros((SIZE+2,SIZE+2))
source[SIZE//2, SIZE//2] = 200
while running:
    dt = 0.016
    print(dt)

    fluidSolver.step(dt,source)
    renderer.draw(fluidSolver.get_density())

    if keyboard.is_pressed('q'):
        running = False

