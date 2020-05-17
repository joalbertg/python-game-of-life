import numpy as np

class GameOfLife:
    def __init__(self, variant = '23/3', nx_c = 100, ny_c = 100, width = 1000, height = 1000):
        self.current_variant(variant) 
        self.nx_c = nx_c
        self.ny_c = ny_c
        self.dim_cw = width / self.nx_c
        self.dim_ch = height / self.ny_c
        self.reset_game_state()

    def current_variant(self, variant):
        self.variant = variant
        first, last = self.variant.split('/')
        self.not_death = list(map(float, first))
        self.create = list(map(float, last))

    def reset_game_state(self):
        # Estado de las celdas. Vivas = 1, Muertas = 0.
        self.game_state = np.zeros((self.nx_c, self.ny_c))

    def polygon(self, x, y):
        # Creamos el polself.ígono de cada celda a dibujar.
        return [((x)     * self.dim_cw, y       * self.dim_ch),
                ((x + 1) * self.dim_cw, y       * self.dim_ch),
                ((x + 1) * self.dim_cw, (y + 1) * self.dim_ch),
                ((x)     * self.dim_cw, (y + 1) * self.dim_ch)]

    def seed(self, entity, pos_x, pos_y):
        len_x, len_y = entity.dim()

        for j in range(0, len_y): # Height / row 
            for i in range(0, len_x): # Width / col
               if entity.model[j][i]:
                   self.game_state[i + pos_x, j + pos_y] = 1

    def vicinity(self, x, y):
        # Calculamos el número de vecinos cercanos.
        return self.game_state[(x - 1) % self.nx_c, (y - 1) % self.ny_c] + \
               self.game_state[(x)     % self.nx_c, (y - 1) % self.ny_c] + \
               self.game_state[(x + 1) % self.nx_c, (y - 1) % self.ny_c] + \
               self.game_state[(x - 1) % self.nx_c, (y)     % self.ny_c] + \
               self.game_state[(x + 1) % self.nx_c, (y)     % self.ny_c] + \
               self.game_state[(x - 1) % self.nx_c, (y + 1) % self.ny_c] + \
               self.game_state[(x)     % self.nx_c, (y + 1) % self.ny_c] + \
               self.game_state[(x + 1) % self.nx_c, (y + 1) % self.ny_c]

