import urllib2
import re

filePath = "http://rate.bot.com.tw/xrt/fltxt/0/day"
data = urllib2.urlopen(filePath)

for line in data:
    print check_string(line)

def check_string(input):
    regex = r"^[A-Z][A-Z][A-Z]"
    matches = re.finditer(regex, input)
    return matches
