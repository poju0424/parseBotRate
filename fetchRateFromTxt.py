import urllib2
import re
import urlparse
import cgi
import logging
from datetime import datetime
from socket import error as SocketError

logging.basicConfig()
updateTime = 0

def GetFileName(url):
    response = urllib2.urlopen(url)
    _, params = cgi.parse_header(response.headers.get('Content-Disposition', ''))
    response.close()
    return params['filename']

def CheckString(input):
    regex = r"^[A-Z][A-Z][A-Z]"
    matches = re.match(regex, input)
    return matches

def ConnectPSQL(currency, cashBuy, cashSell, rateBuy, rateSell, nowtime):
    urlparse.uses_netloc.append("postgres")
    url = urlparse.urlparse(os.environ["DATABASE_URL"])
    cnx = psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port
    )
    cursor = cnx.cursor()
    tableName = "bot"+"_"+currency.lower()
    cursor.execute(" INSERT INTO "+tableName+" (cashBuy, cashSell, rateBuy, rateSell, datetime) VALUES (%s, %s, %s, %s, %s) ", (cashBuy, cashSell, rateBuy, rateSell, nowtime))
    print("fetch complete!"+"("+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+")")
    cnx.commit()
    cursor.close()
    cnx.close()
	
def FetchRate():
    global updateTime
    filePath = "http://rate.bot.com.tw/xrt/fltxt/0/day"
    #ex: ExchangeRate@201703201542.txt
    
    newUpdateTime = GetFileName(filePath)[13:-4]
    print (newUpdateTime)
    if updateTime == newUpdateTime:
        print ("No new rate data")
    else:
        updateTime = newUpdateTime
        data = urllib2.urlopen(filePath)
 
        for line in data:
            if CheckString(line):
                arr = line.split()
                nowtime = datetime.strptime("".join(nowUpdateTime[0]), '%Y/%m/%d %H:%M')
                # ConnectPSQL(arr[0], arr[2], arr[12], arr[3], arr[13])
                print (arr[0], arr[2], arr[12], arr[3], arr[13])
        data.close()
# FetchRate()
try:		
    FetchRate()
except SocketError as e:
    print ("Connection failed, retrying")
    FetchRate()
except:
    print("Unexpected error, retrying")
    FetchRate()