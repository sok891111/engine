"""Spawn multiple workers and wait for them to complete"""
# from __future__ import print_function
import sys
from httphandler import Http
urls = [ 'http://192.168.0.10']

import gevent
from gevent import monkey

# patches stdlib (including socket and ssl modules) to cooperate with other greenlets
monkey.patch_all()
from urllib2 import urlopen

def test(url):
    try:
        Http(url,8080)
    except Exception, why:
        print why 
        

jobs = [gevent.spawn(test, url) for url in urls]

gevent.wait(jobs)