import asyncore
import asynchat
import time
import socket
 
connections_processed = 0
 
 
class AServerHandler(asynchat.async_chat):
 
    # def __init__(self, sock, addr, sessions, log):
    def __init__(self, sock, timeout=10):
        asynchat.async_chat.__init__(self, sock=sock)
        self.last_read = time.time()
        self.timeout = timeout
        #self.addr = addr
        #self.sessions = sessions
        self.ibuffer = []
        self.set_terminator(b"\n")
        #self.log = log
        self.state = 0
        global connections_processed
        connections_processed = connections_processed + 1
        self.cid = connections_processed
        self.push(str.encode(
                  "Hello Connection %d!\r\n" % connections_processed))
 
    def collect_incoming_data(self, data):
        """Buffer the data"""
        self.ibuffer.append(data)
 
    def readable(self):
        if time.time() - self.last_read > self.timeout:
            return False
        return asynchat.async_chat.readable(self)
 
    def writable(self):
        if time.time() - self.last_read > self.timeout:
            self.handle_timeout()
            return False
        return asynchat.async_chat.writable(self)
 
    def found_terminator(self):
        self.last_read = time.time()
        print(self.ibuffer)
        self.push(b"OK\n")
        self.ibuffer = []
 
    def handle_timeout(self):
        print("Connection %d Timeout" % self.cid)
        self.handle_close()
 
    def handle_close(self):
        print("Connection %d CLOSED" % self.cid)
        self.close()
 
 
class AServer(asyncore.dispatcher):
 
    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.connect((host, 21))
        self.listen(5)
 
    def handle_accepted(self, sock, addr):
        print('Incoming connection from %s' % repr(addr))
        self.handler = AServerHandler(sock)
 
server = AServer('67.128.230.124', 21)
asyncore.loop(timeout=1)