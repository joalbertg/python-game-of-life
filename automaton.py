import numpy as np

class Automaton:
    def __init__(self, pos_x = 0, pos_y = 0):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def dim(self):
        return (len(self.model[0]), len(self.model))

    def rot90(self, times = 1):
        self.model = np.rot90(self.model, times)


