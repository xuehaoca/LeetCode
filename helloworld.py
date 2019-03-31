#!/usr/bin/python
import urllib2
import os
import sys
import re

req = urllib2.urlopen('https://www.bureau.tohoku.ac.jp/shisan/campusbus/oshirase13.pdf')
buf = req.read()
url = 'https://www.bureau.tohoku.ac.jp/shisan/campusbus/oshirase13.pdf'
listurl = re.findall('',buf)
print url

def getFile(url):
    file_name = url.split('/')[-1]
    u = urllib2.urlopen(url)
    f = open(file_name, 'wb')
    print file_name
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break
        f.write(buffer)
    f.close()
    #print "Sucessful to download" + " " + file_name

getFile(url)
             
