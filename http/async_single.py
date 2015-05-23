import asyncore, socket, time
""" single threaded async """
class HTTP(asyncore.dispatcher):

    def __init__(self, host, path):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.test_host = host
        self.connect( (host, 80) )
        self.buffer = 'HEAD %s HTTP/1.0\r\n\r\n' % path

    def handle_connect(self):
        pass

    def handle_close(self):
        self.close()
        print self.test_host

    def handle_read(self):
        self.recv(8192)


    def writable(self):
        return (len(self.buffer) > 0)

    def handle_write(self):
        sent = self.send(self.buffer)
        self.buffer = self.buffer[sent:]


start = time.time()
hosts = ["www.yahoo.com", "www.google.com", "www.amazon.com",
        "www.ibm.com", "www.apple.com"]
for host in hosts:
	client = HTTP(host, '/')	

asyncore.loop()
print "Elapsed Time: %s" % (time.time() - start)