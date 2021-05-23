from .guibase import GUIBase
import pygame
import pygame.locals

class GUI(GUIBase):
    def __init__(self):
        super().__init__((100,100))
        self._state = 'stop'
        self._is_empty = True

    def gui_event(self, event):
        if event.type == pygame.locals.QUIT:
            self.gui_running = False
        elif event.type == pygame.locals.KEYDOWN:
            if event.key == pygame.locals.K_1:
                if self._state == 'stop':
                    self._is_empty = True
                    self.cb_reset()
                else:
                    self._state = 'stop'
                    self.cb_stop()
            elif event.key == pygame.locals.K_2:
                if self._is_empty:
                    self._is_empty = False
                    self._state = 'record'
                    self.cb_rec()
                elif self._state == 'record':
                    self._state = 'play'
                    self.cb_play()
                elif self._state == 'play':
                    self._state = 'overdub'
                    self.cb_overdub()
                elif self._state == 'overdub':
                    self._state = 'play'
                    self.cb_play()
                elif self._state == 'stop':
                    self._state = 'play'
                    self.cb_play()
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

    def cb_reset(self):
        raise NotImplementedError

    def cb_getposition(self):
        raise NotImplementedError
