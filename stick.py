from automaton import Automaton

class Stick(Automaton):
    # Autómata palo.
    def __init__(self, pos_x = 0, pos_y = 0):
        super(Stick, self).__init__(pos_x, pos_y)

    model = [[1],
             [1],
             [1]]

