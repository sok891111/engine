import core, json,base64

class Request:

	""" Request class"""

	# url : request url
	# call super class __init__
	def __init__(self, host=None,port=80,headers={},path="/", admin=False):
		self.host = host
		self.port = port
		self.headers=headers
		self.path = path
		self.admin =admin

	def add_header(self, header):
		if not type(header) is dict:
			return
		for key in header.keys():
			self.headers[key] = header[key]

	def convert_request_header(self):
		#HTTP/1.1 Get request
		header="GET %s HTTP/1.1\r\nHOST: %s" % (self.path,self.host)
		_header=self.headers
		for key in _header.keys():
			header+="\r\n"+key+": "+_header[key]
		header+="\r\n\r\n"
		return header

	def __getattr__(self,name):
		try:
			return self.__dict__[name]
		except KeyError:
			return None

class Response:
	"""Response class"""

	def __init__(self, request, raw):
		self.raw = raw
		self.request = request
		self.status_code = 0
		self.header = self.set_responseHeaders(self.raw)

	def set_responseHeaders(self,raw):
		headers = {}
		lines = self.raw.split("\r\n")
		for i, line in enumerate(lines):
			# find out http status code
			if i == 0 : 
				self.status_code = self.parse_status_code(line)
				continue  
			_line = line.replace(" ","")
			_headline = _line.split(":",1)
			headers[_headline[0].lower()] = _headline[1].lower()
		return headers

	def parse_status_code(self,line):
		try:
			line = line.split(" ")
			return int(line[1])
		except Exception, why :
			print why

	def is_success(self):
		# if it is bad request, return false;
		if self.status_code <400 :
			return True;
		else :
			return False;


	def retrieve_server_info(self):
		self.server="";
		# ServerInfo
		# first find out "x-powered-by" field from response header
		if self.header.get("x-powered-by"):
			temp =self.header.get("x-powered-by").lower();

			# if there is "x-powered-by" field then find out server name
			# add different server name logic from here
			if temp.find("jboss".lower()) > 0:
				self.server = "jboss";
			elif temp.find("tomcat".lower()) > 0:
				self.server = "tomcat";
			else :
				self.server = self.header.get("x-powered-by");
		elif self.header.get("server"):
			self.server = self.header.get("server");
		return self.server;

	def redirect(self, location):
		req = Request(location)
		core.HTTPClient(req)


	def secure_server(self):
		if not self.is_success : return
		server = Server(self.request, self)
		server._access_server()


class Server:

	def __init__(self, request, response):
		self.request = request
		self.response = response
		self.pwlist = {}
	def _access_server(self):

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


