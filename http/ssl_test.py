"""Spawn multiple workers and wait for them to complete"""
# from __future__ import print_function
import sys
from httphandler import Response
urls = [ 'https://www.slack.com','http://www.naver.com','http://www.daum.net']

import gevent
from gevent import monkey

# patches stdlib (including socket and ssl modules) to cooperate with other greenlets
monkey.patch_all()
from urllib2 import urlopen

def print_head(url):
    print 'Starting %s' % url
    try:
        res = Response(urlopen(url))
    except Exception, why:
        print why 
        return
    print "%s %s"%(res.request_url,res.getheader("server")) 

jobs = [gevent.spawn(print_head, url) for url in urls]

gevent.wait(jobs)