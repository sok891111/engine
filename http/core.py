import asyncore, socket
from httphandler import Request,Response
""" single threaded async """
###
###  check handle_read
###  most biz logic is located at handle_read func
###

class HTTPClient(asyncore.dispatcher):

    def __init__(self, request):

        asyncore.dispatcher.__init__(self)

        self.request = request
        self.response = None

        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.connect( (self.request.host, self.request.port) )
        except socket.error,why:
            print why  # No host there
        header = self.request.convert_request_header()
        self.buffer = header

    def handle_connect(self):
        pass

    def handle_close(self):
        self.close()

        # Reading raw response and convert response obj
        # execute request.callback()
        # callback func determine server and
        # try logging default server admin
    def handle_read(self):
        sentence = self.recv(2048)
        self.close()
        raw = sentence.split("\r\n\r\n")[0]
        self.response = Response(self.request, raw)

        # admin
        if self.request.admin :
            print self.response.is_success()
            print self.request.host
            print self.response.header
        else:
            #location -> redirect
            if self.response.header.get("location") :
                pass
                # print self.response.header.get("location")
                # self.response.redirect(self.response.header.get("location"))
            self.response.secure_server()

    def writable(self):
        return (len(self.buffer) > 0)

    def handle_write(self):
        sent = self.send(self.buffer)
        self.buffer = self.buffer[sent:]

    def __getattr__(self,name):
        try:
            return self.__dict__[name]
        except KeyError:
            return None

