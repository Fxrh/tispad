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


import socketserver
import queue

class TispaServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    
    def __init__(self, server_address, data_q, bind_and_activate=True):
        socketserver.TCPServer.__init__(self, server_address, TispaHandler, bind_and_activate)
        self.queue = data_q
    
    def process_request_thread(self, request, client_address):
        print("blub")
        handler = TispaHandler( request, client_address, self, self.queue )
        handler.setup()
        handler.handle()
        handler.finish()

class TispaHandler( socketserver.StreamRequestHandler ):
    
    def __init__(self, request, client_address, server):
        raise Exception()
    
    def __init__(self, request, client_address, server, data_q):
        self.data = data_q
        print("bla")
        socketserver.StreamRequestHandler.__init__(self, request, client_address, server )
    
    def handle(self):
        while( True ):
            data = self.rfile.readline()
            self.wfile.write(data.upper())
            self.data.put(data)
        
if __name__ == '__main__':
    HOST, PORT = "localhost", 9999
    queue = queue.Queue()
    server = TispaServer( (HOST, PORT), queue )
    server.serve_forever()
    