import pygame
import numpy as np
import time

pygame.init()

# Ancho y alto de la pantalla.
width, height = 800, 800
# creación de la pantalla.
screen = pygame.display.set_mode((height, width))

# Color dle fondo = Casi negro, casi oscuro.
bg = 25, 25, 25
# Pintamos el fondo con el color elegido.
screen.fill(bg)

nxC, nyC = 100, 100

dimCW = width / nxC
dimCH = height / nyC
sleep = 0.1
variant = '23/3'
# variant = '1357/1357'
# variant = '235678/3678'
# variant = '34/34'
# variant = '4/2'
# variant = '51/346'
notDeath, create = variant.split('/')

# Estado de las celdas. Vivas = 1, Muertas = 0.
gameState = np.zeros((nxC, nyC))

# Autómata palo.
stick = [[1],
         [1],
         [1]]

stickPosX = 5
stickPosY = 3

# Autómata movil.
spaceship = [[0, 1, 0],
             [0, 0, 1],
             [1, 1, 1]]

spaceshipPosX = 20
spaceshipPosY = 21

# Autómata pistola d eplaneadores.
spaceshipGuns = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                 [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
spaceshipGunsPosX = 50
spaceshipGunsPosY = 50

# Autómata oscilador.
doubleEight = [[0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
               [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
               [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0]]
doubleEightPosX = 50
doubleEightPosY = 10

def __seed__(model, posX, posY, origin):
    for i in range(0, len(model)): # Height / row
       for j in range(0, len(model[0])): # Width / col
           if model[i][j]:
               origin[j + posX, i + posY] = 1

__seed__(stick, stickPosX, stickPosY, gameState)
# __seed__(spaceship, spaceshipPosX, spaceshipPosY, gameState)
__seed__(spaceshipGuns, spaceshipGunsPosX, spaceshipGunsPosY, gameState)
__seed__(doubleEight, doubleEightPosX, doubleEightPosY, gameState)

# spaceship = np.rot90(spaceship)

# Control de la ejecución del juego.
pauseExect = False

# Bucle de ejecición.
while True:
    newGameState = np.copy(gameState)
    screen.fill(bg)
    # time.sleep(sleep)

    # Registramos eventos de teclado y ratón.
    ev = pygame.event.get()

    for event in ev:
        # Detectamos si se presiona una tecla.
        if event.type == pygame.KEYDOWN:
            pauseExect = not pauseExect
        # Detectamos si se presiona el ratón.
        mouseClick = pygame.mouse.get_pressed()

        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
            newGameState[celX, celY] = not mouseClick[2] 

    for y in range(0, nxC):
        for x in range(0, nyC):
            if not pauseExect:
                # Calculamos el número de vecinos cercanos.
                n_neigh = gameState[(x - 1) % nxC, (y - 1) % nyC] + \
                          gameState[(x)     % nxC, (y - 1) % nyC] + \
                          gameState[(x + 1) % nxC, (y - 1) % nyC] + \
                          gameState[(x - 1) % nxC, (y)     % nyC] + \
                          gameState[(x + 1) % nxC, (y)     % nyC] + \
                          gameState[(x - 1) % nxC, (y + 1) % nyC] + \
                          gameState[(x)     % nxC, (y + 1) % nyC] + \
                          gameState[(x + 1) % nxC, (y + 1) % nyC]
                # 23/3 Rule 1: Una célula muerta con exactamente 3 vecinas vivas, "revive".
                if gameState[x, y] == 0 and str(int(n_neigh)) in create:
                    newGameState[x, y] = 1
                # 23/3 Rule 2: Una célula viva con menos de 2 o más de 3 vacinas vivias, "muere".
                elif gameState[x, y] == 1 and not str(int(n_neigh)) in notDeath:
                    newGameState[x, y] = 0

            # Creamos el polígono de cada celda a dibujar.
            poly = [((x)     * dimCW, y       * dimCH),
                    ((x + 1) * dimCW, y       * dimCH),
                    ((x + 1) * dimCW, (y + 1) * dimCH),
                    ((x)     * dimCW, (y + 1) * dimCH)]
            # Y dibujamos la celda para cada par de x e y.
            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 0)
    # Actualizamos el estado del juego.
    gameState = np.copy(newGameState)
    pygame.display.flip()

