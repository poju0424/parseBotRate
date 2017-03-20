import urllib2
import re
import urlparse
import cgi
import logging

logging.basicConfig()
fileName = ""

def GetFileName(url):
    response = urllib2.urlopen(url)
    return response.info().headers

def CheckString(input):
    regex = r"^[A-Z][A-Z][A-Z]"
    matches = re.match(regex, input)
    return matches

def FetchRate():
    global fileName
	
    filePath = "http://rate.bot.com.tw/xrt/fltxt/0/day"
    print GetFileName(filePath)
    data = urllib2.urlopen(filePath)
    bankName = "bot"

    for line in data:
        if CheckString(line):
            print line.split()
