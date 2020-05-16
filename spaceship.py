class Spaceship:
    # Autómata planeadores.
    def __init__(self, posX = 0, posY = 0):
        self.posX = posX
        self.posY = posY

    __model = [[0, 1, 0],
               [0, 0, 1],
               [1, 1, 1]]

    def model(self):
        return self.__model

