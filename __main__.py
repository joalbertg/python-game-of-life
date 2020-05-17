from screen_pg import ScreenPg
from event_pg import EventPg
from game_of_life import GameOfLife
from spaceship_guns import SpaceshipGuns
from spaceship import Spaceship
from oscillator import Oscillator
from stick import Stick
from sys import exit
import numpy as np

spg = ScreenPg()
epg = EventPg(spg.pg)
gol = GameOfLife()

spg.beggin()
spg.set_title('Game of Life')

# variant = '23/3'
# variant = '1357/1357'
# variant = '235678/3678'
# variant = '34/34'
# variant = '4/2'
# variant = '51/346'

class Game:
    def __init__(self, gol):
        self.gol = gol
        # Control de la ejecución del juego.
        self.pause_exec = False

    def do_pause(self):
        self.pause_exec = not self.pause_exec

    def scene(self):
        spaceships_guns = [(10, 0), (gol.nx_c - 46, gol.ny_c - 9)]
        for i in range(len(spaceships_guns)):
            spaceship_guns = SpaceshipGuns(spaceships_guns[i][0], spaceships_guns[i][1])
            if (i % 2) == 1:
                spaceship_guns.rot90(2)
            gol.seed(spaceship_guns, spaceship_guns.pos_x, spaceship_guns.pos_y)

        oscillators = [(gol.nx_c - 27, 10), (10, gol.ny_c - 27)]
        for i in oscillators:
            oscilltor = Oscillator(i[0], i[1])
            gol.seed(oscilltor, oscilltor.pos_x, oscilltor.pos_y)

        sticks = [(5, 10), (5, 20), (gol.nx_c - 6, gol.ny_c - 11), (gol.nx_c - 6, gol.ny_c - 21)]
        for i in sticks:
            stick = Stick(i[0], i[1])
            gol.seed(stick, stick.pos_x, stick.pos_y)

        spaceships = [Spaceship(40, 80)]
        spaceships[0].rot90()
        gol.seed(spaceships[0], spaceships[0].pos_x, spaceships[0].pos_y)

game = Game(gol)
game.scene()

# Bucle de ejecición.
running = True
while running:
    ev = epg.get_event()
    running = not epg.event_close(ev)

    new_game_state = np.copy(gol.game_state)
    spg.set_background()

    if epg.pause_exec(ev):
        game.do_pause()

    mouseClick = epg.do_mouse_pressed()

    if sum(mouseClick) > 0:
        pos_x, pos_y = epg.mouse_get_pos()
        cel_x, cel_y = int(np.floor(pos_x / gol.dim_cw)), int(np.floor(pos_y / gol.dim_ch))
        new_game_state[cel_x, cel_y] = not mouseClick[2] 

    for y in range(0, gol.ny_c):
        for x in range(0, gol.nx_c):
            if not game.pause_exec:
                n_neigh = int(gol.vicinity(x, y))
                # 23/3 Rule 1: Una célula muerta con exactamente 3 vecinas vivas, "revive".
                if gol.game_state[x, y] == 0 and n_neigh in gol.create:
                    new_game_state[x, y] = 1
                # 23/3 Rule 2: Una célula viva con menos de 2 o más de 3 vacinas vivias, "muere".
                elif gol.game_state[x, y] == 1 and not n_neigh in gol.not_death:
                    new_game_state[x, y] = 0

            poly = gol.polygon(x, y)
            # Y dibujamos la celda para cada par de x e y.
            if new_game_state[x, y] == 1:
                spg.draw_polygon((31, 184, 163), poly, 1)
    # Actualizamos el estado del juego.
    gol.game_state = np.copy(new_game_state)
    spg.update()
exit()

