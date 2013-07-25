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
import ncserver
import queue


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
        self.allowedList = []
        
        
    def parseCommand(self, command):
        if command.strip() == '':
            return
        command = command.decode().split()
        print(command)
        if command[0].lower() == "tofullscreen" and len(command) == 2:
            try:
                cell = int(command[1])
            except ValueError:
                return
            print(self.wm.toFullscreen( cell ))
        elif command[0].lower() == "endfullscreen" and len(command) == 1:
            self.wm.endFullscreen()
        elif command[0].lower() == "setcolsrows" and len(command) == 3:
            try:
                cols = int(command[1])
                rows = int(command[2])
            except ValueError:
                return
            self.wm.setColsRows(cols, rows)
        elif command[0].lower() == "start" and len(command) >= 3:
            try:
                cell = int(command[1])
                self.wm.setReplace(cell)
                if command[3] in self.allowedList:
                    subprocess.Popen(command[2:])
            except:
                return


def main():
    data_q = queue.Queue()
    ncs = ncserver.TispaServer( ("localhost", 48738), data_q )
    ncs.timeout = 1
    wc = WindowController()
    while True:
        ncs.handle_request()
        if not data_q.empty():
            wc.parseCommand( data_q.get() )

if __name__ == '__main__':
    main()
        
