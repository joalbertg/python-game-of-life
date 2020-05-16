class EventPg:
    def __init__(self, pg):
        self.pg = pg

    def get_event(self):
        return self.pg.event.get()

    def event_keydown(self, type):
        if type == self.pg.KEYDOWN:
            return True
        return False

    def event_close(self, ev):
        # Detectamos si se presiona esc o hacen click sobre close.
        for event in ev:
            type = event.type
            if (self.event_keydown(type) and event.key == self.pg.K_ESCAPE) or type == self.pg.QUIT:
                return True
        return False

    def listen(self, ev, fr, spg):
        for event in ev:
            if self.event_keydown(event.type):
                key = event.key

                if self.is_key(key):
                    mods = self.pg.key.get_mods()

                    if key == self.pg.K_UP:
                        fr.up_height(spg.height)
                    elif key == self.pg.K_DOWN:
                        fr.down_height(spg.height)
                    elif key == self.pg.K_LEFT:
                        fr.left_width(spg.width)
                    elif key == self.pg.K_RIGHT:
                        fr.right_width(spg.width)
                    elif key == self.pg.K_n or key == self.pg.K_m:
                        if mods & self.pg.KMOD_LSHIFT or mods & self.pg.KMOD_CAPS:
                            if key == self.pg.K_n:
                                fr.up_rule()
                            elif key == self.pg.K_m:
                                fr.up_10_rule()
                        elif key == self.pg.K_n:
                            fr.down_rule()
                        elif key == self.pg.K_m:
                            fr.down_10_rule()
                    return True
        return False

    def is_key(self, key):
        if key in [self.pg.K_UP, self.pg.K_DOWN, self.pg.K_LEFT, self.pg.K_RIGHT, 
                   self.pg.K_n, self.pg.K_m]:
            return True
        return False

    def pause_exec(self, ev):
        for event in ev:
            # Detectamos si se presiona una tecla.
            if self.event_keydown(event.type) and event.key == self.pg.K_SPACE:
                return True
        return False

    def do_mouse_pressed(self):
        # Detectamos si se presiona el ratón.
        return self.pg.mouse.get_pressed()

    def mouse_get_pos(self):
        return self.pg.mouse.get_pos()

