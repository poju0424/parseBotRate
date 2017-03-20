import urllib2

filePath = "http://rate.bot.com.tw/xrt/fltxt/0/day"
data = urllib2.urlopen(filePath)
f.close()

for line in data:
    print line


