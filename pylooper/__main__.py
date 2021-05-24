from .aw_looper import Looper
from .gui import GUI
from .configuration import config_read

class GUI(GUI):
    def cb_stop(self):
        looper.stop()

    def cb_rec(self):
        looper.record()

    def cb_play(self):
        looper.play()

    def cb_overdub(self):
        looper.overrec()

    def cb_getposition(self):
        return looper.getposition()

if __name__ == "__main__":

    conf = config_read()
    GUI.gui_init()

    looper = Looper(conf['Audio'])
    gui = GUI(conf['Keymaps'])
    
    if not looper.aw_init():
        quit(1)

    looper.aw_start()
    gui.gui_run()

    GUI.gui_deinit()
    looper.aw_stop()
