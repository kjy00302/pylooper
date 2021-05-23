from .aw_looper import Looper
from .gui import GUI

class GUI(GUI):
    def cb_stop(self):
        looper.stop()

    def cb_rec(self):
        looper.record()

    def cb_play(self):
        looper.play()

    def cb_overdub(self):
        looper.overrec()

    def cb_reset(self):
        looper.reset()

    def cb_getposition(self):
        return looper.getposition()

if __name__ == "__main__":
    looper = Looper()
    if not looper.aw_init():
        quit(1)

    GUI.gui_init()
    gui = GUI()

    looper.aw_start()
    gui.gui_run()

    GUI.gui_deinit()
    looper.aw_stop()
