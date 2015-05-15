import asyncore, socket, time
from httphandler import Request,Response
""" single threaded async """
class HTTPClient(asyncore.dispatcher):

    def __init__(self, request):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.connect( (request.host, 80) )
        except socket.gaierror,why:
            # No host there
            print why
        header = self.makeHeader(request)
        self.buffer = header

    def handle_connect(self):
        pass

    def handle_close(self):
        self.close()
        print "asdf"

    def handle_read(self):
        print self.recv(2048)
        self.close()

    def writable(self):
        return (len(self.buffer) > 0)

    def handle_write(self):
        sent = self.send(self.buffer)
        self.buffer = self.buffer[sent:]

    def makeHeader(self, request):
        #HTTP/1.1 Get request
        header="GET %s HTTP/1.1\r\nHOST: %s" % (request.path,request.host)
        _header=request.headers
        for key in _header.keys():
            header+="\r\n"+key+": "+_header[key]
        header+="\r\n\r\n"
        return header
    def __getattr__(self,name):
        try:
            return self.__dict__[name]
        except KeyError:
            return None

start = time.time()
# hosts = ["www.yahoo.com", "www.google.com", "www.amazon.com",
#         "www.ibm.com", "www.apple.com"]
hosts = ["www.amazon.com"]


for host in hosts:
    req = Request(host)
    client = HTTPClient(req)    
    # while(not client.done):
    #     response = client.response
    # print response

asyncore.loop()
print "Elapsed Time: %s" % (time.time() - start)