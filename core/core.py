import asyncore, socket, time
""" single threaded async """
class core(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect( (host, port) )
        
    def handle_connect(self):
        pass

    def handle_close(self):
        pass

    def handle_read(self):
        self.recv(8192)

    def writable(self):
        return (len(self.buffer) > 0)

    def handle_write(self):
        sent = self.send(self.buffer)
        self.buffer = self.buffer[sent:]


# client = core("67.128.230.124", 21,"")    

