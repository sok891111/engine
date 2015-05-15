class Request:

	""" Request class"""

	# url : request url
	# call super class __init__
	def __init__(self, host=None,headers={},path="/"):
		self.host = host
		self.headers=headers
		self.path = path

	def addHeader(self, header):
		if not type(header) is dict:
			return
		for key in header.keys():
			self.headers[key] = header[key]

	def __getattr__(self,name):
		try:
			return self.__dict__[name]
		except KeyError:
			return None
class Response:
	def __init__(self):
		return

if __name__ == "__main__":
	test ={}
	print test.keys()
	req = Request("test",{"test":"test","a" :"d"})
	req.addHeader({"t" :"a"})
	print req.header

