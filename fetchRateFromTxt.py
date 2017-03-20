import urllib2
import re

def CheckString(input):
    regex = r"^[A-Z][A-Z][A-Z]"
    matches = re.match(regex, input)
    return matches

filePath = "http://rate.bot.com.tw/xrt/fltxt/0/day"
data = urllib2.urlopen(filePath)

for line in data:
    print CheckString(line)


