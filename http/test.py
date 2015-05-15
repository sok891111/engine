import urllib2
for x in xrange(1,3):
	req = urllib2.Request('http://www.google.com/')
	r = urllib2.urlopen(req)
	print "";
	print r.read()