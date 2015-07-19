import sys,string
import json
import gevent
from gevent import monkey
monkey.patch_all()
import urllib2 
_web_console = (('tomcat','admin/'),('tomcat','manager/'),('tomcat','master/'),
				('tomcat','manual/'),('tomcat','system/'),
				('WebLogic','AdminMain/'),('WebLogic','AdminProps/'),
				('WebLogic','AdminRealm/'),('WebLogic','console/'),				
				('WebSphere','adminconsole/'),('WebSphere','jmx-console/'),
				('JBOSS','web-console/'),('Jeus','webadmin/'))

_passwd_file = 'passwd.json'

class Http:
    def __init__(self, url,port):
        self.url = url
        self.port = str(port)
        self.passwds = self.read_jsonfile(_passwd_file)
        jobs = [gevent.spawn(self.do_http,path) for path in _web_console]
        gevent.wait(jobs)

    
    def do_http(self,path):
        was_info = path[0].lower()
        test_url = self.url+":"+self.port+"/"+path[1]
        result = self.find_console(test_url)
        if result:
            pw = self.get_defaultpw(was_info)
            self.try_access(was_info,test_url,pw)

    def read_jsonfile(self,filename):
        f=None
        try:
            f = open(filename,'r')
            data = json.loads(f.read())
            f.close()
        except Exception, why:
            f.close()
        return data

    def find_console(self,url):
        try:
            urllib2.urlopen(url,None,1)
            return True
        except urllib2.HTTPError, e:
            if e.code != 404:
                return True 
            else:
                return False
        except urllib2.URLError, e:
            return False


    def get_defaultpw(self,was):
        try:
            return self.passwds[was]
        except Exception, e:
            return {"admin":"admin"}


    def try_access(self, wastype, url, pw):
        if wastype == 'tomcat':
            passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
            for key in pw:
                passman.add_password(None, url, key, pw[key])
            authhandler = urllib2.HTTPBasicAuthHandler(passman)
            opener = urllib2.build_opener(authhandler)
            try:
                pagehandle = opener.open(url)
            except Exception , why:
                print why


