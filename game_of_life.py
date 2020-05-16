from screen_pg import ScreenPg
from event_pg import EventPg
from spaceship_guns import SpaceshipGuns
from spaceship import Spaceship
from oscillator import Oscillator
from stick import Stick
from sys import exit
import numpy as np
import time

spg = ScreenPg()
epg = EventPg(spg.pg)


spg.beggin()
spg.set_title('Game of Life')

nxC, nyC = 100, 100

dimCW = spg.width / nxC
dimCH = spg.height / nyC
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
# models
spaceship_guns = SpaceshipGuns(0, 0)
spaceship = Spaceship(40, 80)
stick = Stick(0, 30)

def __seed__(model, posX, posY, origin):
    for i in range(0, len(model)): # Height / row
       for j in range(0, len(model[0])): # Width / col
           if model[i][j]:
               origin[j + posX, i + posY] = 1

__seed__(stick.model(), stick.posX, stick.posY, gameState)
__seed__(np.rot90(spaceship.model()), spaceship.posX, spaceship.posY, gameState)
__seed__(spaceship_guns.model(), spaceship_guns.posX, spaceship_guns.posY, gameState)

oscillators = [(nxC - 17, 4), (4, nyC - 17)]
for coors in oscillators:
    oscilltor = Oscillator(coors[0], coors[1])
    __seed__(oscilltor.model(), oscilltor.posX, oscilltor.posY, gameState)

# spaceship = np.rot90(spaceship)

# Control de la ejecución del juego.
pauseExect = False

# Bucle de ejecición.
running = True
while running:
    ev = epg.get_event()
    running = not epg.event_close(ev)

    newGameState = np.copy(gameState)
    spg.set_background()
    # time.sleep(sleep)

    if epg.pause_exec(ev):
        pauseExect = not pauseExect

    mouseClick = epg.do_mouse_pressed()

    if sum(mouseClick) > 0:
        posX, posY = epg.mouse_get_pos()
        celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
        newGameState[celX, celY] = not mouseClick[2] 

    for y in range(0, nyC):
        for x in range(0, nxC):
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
                spg.draw_polygon((128, 128, 128), poly, 1)
            else:
                spg.draw_polygon((128, 128, 128), poly, 0)
    # Actualizamos el estado del juego.
    gameState = np.copy(newGameState)
    spg.update()
exit()

