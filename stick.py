class Stick:
    # Autómata palo.
    def __init__(self, posX = 0, posY = 0):
        self.posX = posX
        self.posY = posY

    __model = [[1],
               [1],
               [1]]

    def model(self):
        return self.__model

