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
<<<<<<< HEAD
    def __init__(self, res):
        self.res = res
=======

	def __init__(self, request, response):
		self.request = request
		self.response = response
		self.pwlist = {}
	def _access_server(self):
		#Server Logic
		server = self.response.retrieve_server_info()
		servername = ""
		if "tomcat" in server   :
			servername = "tomcat"
			suffix = "/manager/";
		elif "apache" in server   :
			servername = "tomcat"
			suffix = "/manager/";
		else :
			suffix = "/manager/";

		req = Request(self.request.host, 8080, {},path=suffix, admin=True)

		## copy python authentication sample
		self.pwlist = self.get_passwordList().get(servername);

		if not self.pwlist : return

		## add passwd list from config file
		for key in self.pwlist.keys():
			passwd = key+":"+self.pwlist.get(key)
			encodedpw = base64.b64encode(passwd)
			req.add_header({"Authorization" : encodedpw})
		core.HTTPClient(req)

	def get_passwordList(self):
		pwFile="./passwd.json";
		f = open(pwFile, 'r');
		js = json.loads(f.read());
		f.close();
		return js;

if __name__ == "__main__":
	test ={}
	req = Request("test",{"test":"test","a" :"d"})
	req.add_header({"t" :"a"})


>>>>>>> 10a8b08ae3b81fba1ba1dc131178e131e71a8162
