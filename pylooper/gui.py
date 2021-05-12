from .guibase import GUIBase
import pygame
import pygame.locals

class GUI(GUIBase):
    def __init__(self):
        super().__init__((100,100))

    def gui_event(self, event):
        if event.type == pygame.locals.QUIT:
            self.gui_running = False
        elif event.type == pygame.locals.KEYDOWN:
            if event.key == pygame.locals.K_1:
                self.cb_stop()
            elif event.key == pygame.locals.K_2:
                self.cb_rec()
            elif event.key == pygame.locals.K_3:
                self.cb_play()
            elif event.key == pygame.locals.K_4:
                self.cb_overdub()
            elif event.key == pygame.locals.K_ESCAPE:
                self.gui_running = False

    def gui_process(self):
        pass

    def gui_draw(self, surface):
        surface.fill((255,255,255))

    def cb_stop(self):
        raise NotImplementedError

    def cb_rec(self):
        raise NotImplementedError

    def cb_play(self):
        raise NotImplementedError

    def cb_overdub(self):
        raise NotImplementedError
