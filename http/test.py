import time, core , asyncore
from httphandler import Request,Response

start = time.time()
# hosts = ["www.yahoo.com", "www.google.com", "www.amazon.com",
        # "www.ibm.com", "www.apple.com","www.naver.com","192.168.0.10"]
# hosts = ["www.yahoo.com"]
hosts = ["192.168.0.10"]


for host in hosts:
    req = Request(host,8080)
    client = core.HTTPClient(req)    
    # while(not client.done):
    #     response = client.response
    # print response

asyncore.loop()
print "Elapsed Time: %s" % (time.time() - start)


