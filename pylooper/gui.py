from .guibase import GUIBase
import pygame
import pygame.locals

class GUI(GUIBase):
    def __init__(self):
        super().__init__((150,150))
        self.flag = 'stop'

    def gui_event(self, event):
        if event.type == pygame.locals.QUIT:
            self.gui_running = False
        elif event.type == pygame.locals.KEYDOWN:
            if event.key == pygame.locals.K_1:
                self.cb_stop()
                self.flag = 'stop'
            elif event.key == pygame.locals.K_2:
                self.cb_rec()
                self.flag = 'play'
            elif event.key == pygame.locals.K_3:
                self.cb_play()
                self.flag = 'record'
            elif event.key == pygame.locals.K_4:
                self.cb_overdub()
                self.flag = 'overdub'
            elif event.key == pygame.locals.K_ESCAPE:
                self.gui_running = False

    def gui_process(self):
        pass

    def gui_draw(self, surface):
        surface.fill((255,255,255))
        pygame.draw.rect(
            surface,
            "#0000ff",
            (0,0,150 * self.cb_getposition(),150))
        if self.flag == 'stop':
            pygame.draw.rect(surface, "#000000", (50,50, 50, 50))

        if self.flag == 'play':
            pygame.draw.polygon(surface, "#00ff00", ((50,50), (50,100), (105,75)))

        if self.flag == 'record':
            pygame.draw.circle(surface, "#ff0000", (75,75),50)

        if self.flag == 'overdub':
            pygame.draw.circle(surface, "#00ff00", (75,75),50)
            pygame.draw.polygon(surface, "#ff0000", ((50,50), (50,100), (105,75)))

    def cb_stop(self):
        raise NotImplementedError

    def cb_rec(self):
        raise NotImplementedError

    def cb_play(self):
        raise NotImplementedError

    def cb_overdub(self):
        raise NotImplementedError

    def cb_getposition(self):
        raise NotImplementedError
