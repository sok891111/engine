import sys,string

_web_console = ['admin/','manager/','master/','manual/','system/'
				'AdminMain/','']
class Response:
    def __init__(self,data):
        self.data = data
        self._headers = {}
        self.status_code = data.getcode()
        self.request_url = data.geturl()
        self.setheaders()        

    def setheaders(self):
        if not self.data : return
        meta_data = str(self.data.info()).split("\r\n")
        for line in meta_data :
            if not line : continue
            header = line.translate( None, string.whitespace ).split(":",1)
            self._headers[header[0].lower()] = header[1]

    def getheaders(self):
        return self._headers

    def getheader(self,name):
        return self._headers.get(name.lower())

class Server:
    def __init__(self, res):
        self.res = res
