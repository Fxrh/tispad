# Copyright (c) 2013 Felix Rohrbach <fxrh@gmx.de>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

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
