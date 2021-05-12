import pygame

class GUIBase:
    def __init__(self, dispsize):
        self._displaysurf = pygame.display.set_mode(dispsize, 0, 32)
        self._timer = pygame.time.Clock()
        self.gui_running = True

    @classmethod
    def gui_init(cls):
        pygame.display.init()

    @classmethod
    def gui_deinit(cls):
        pygame.quit()

    def gui_run(self):
        while self.gui_running:
            for event in pygame.event.get():
                self.gui_event(event)
            self.gui_process()
            self.gui_draw(self._displaysurf)
            pygame.display.update()
            self._timer.tick(60)

    def gui_draw(self, surface):
        raise NotImplementedError

    def gui_process(self):
        raise NotImplementedError

    def gui_event(self, event):
        raise NotImplementedError
