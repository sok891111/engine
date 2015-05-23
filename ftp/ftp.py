import asyncore, asynchat
import re, socket

class anon_ftp(asynchat.async_chat):

    def __init__(self, host):
        asynchat.async_chat.__init__(self)

        self.commands = [
            "USER anonymous",
            "PASS anonymous@",
            "PWD",
            "QUIT"
            ]

        self.set_terminator("\n")

        self.data = ""

        # connect to ftp server
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, 22))

    def handle_connect(self):
        # connection succeeded
        pass

    def handle_expt(self):
        # connection failed
        self.close()

    def collect_incoming_data(self, data):
        # received a chunk of incoming data
        self.data = self.data + data

    def found_terminator(self):
        # got a response line
        data = self.data
        if data.endswith("\r"):
            data = data[:-1]
        self.data = ""

        print "S:", data

        if re.match("\d\d\d ", data):
            # this was the last line in this response
            # send the next command to the server
            try:
                command = self.commands.pop(0)
            except IndexError:
                pass # no more commands
            else:
                print "C:", command
                self.push(command + "\r\n")

anon_ftp("128.121.216.148")

asyncore.loop()