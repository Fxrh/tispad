import subprocess
import dbus
import time


class WindowController:
    def __init__(self):
        self.bus = dbus.SessionBus()
        print("Waiting for connection to wm...")
        while(True):
            try:
                self.wm = self.bus.get_object('de.trollhoehle.tispa','/')
                break
            except:
                time.sleep(1)
        print("Connected.")
        
    def showText(self, text, cell):
        self.wm.setReplace(cell)
        subprocess.Popen(['clients/simpletext/simpletext',text])
