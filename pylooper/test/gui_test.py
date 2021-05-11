from ..guibase import GUIBase
import pygame
import pygame.locals
import random

class Mygui(GUIBase):
    def __init__(self, dispsize):
        super().__init__(dispsize)
        self._displaysurf.fill((255,255,255))

    def gui_draw(self, surface):
        
        color = (
            random.randrange(0,256),
            random.randrange(0,256),
            random.randrange(0,256)
        )
        start = (
            random.randrange(0,surface.get_width()),
            random.randrange(0,surface.get_height())
        )
        stop = (
            random.randrange(0,surface.get_width()),
            random.randrange(0,surface.get_height())
        )
        pygame.draw.aaline(surface, color, start, stop)

    def gui_process(self):
        pass

    def gui_event(self, event):
        if event.type == pygame.locals.QUIT:
            self.gui_running = False

GUIBase.gui_init()
gui = Mygui((100, 100))
gui.gui_run()
GUIBase.gui_deinit()
