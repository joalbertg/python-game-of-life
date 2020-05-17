from automaton import Automaton

class Spaceship(Automaton):
    # Autómata planeadores.
    def __init__(self, pos_x = 0, pos_y = 0):
        super(Spaceship, self).__init__(pos_x, pos_y)

    model = [[0, 1, 0],
             [0, 0, 1],
             [1, 1, 1]]

