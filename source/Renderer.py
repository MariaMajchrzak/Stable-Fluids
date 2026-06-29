import matplotlib.pyplot as plt
import numpy as np


class Renderer:
    def __init__(self, size):
        plt.ion()
        self.__image = plt.imshow(np.zeros((size+2,size+2)),origin='lower', vmin=0, vmax=1)

    def draw(self, data):
        self.__image.set_data(data)
        plt.pause(0.001)