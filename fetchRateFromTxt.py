import urllib2
import re
import os
import psycopg2
import urlparse
import cgi
import logging
from datetime import datetime
from socket import error as SocketError
from apscheduler.schedulers.blocking import BlockingScheduler

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
    print("fetch "+currency+" complete!"+"("+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+")")
    cnx.commit()
    cursor.close()
    cnx.close()
	
def FetchRate():
    global updateTime
    filePath = "http://rate.bot.com.tw/xrt/fltxt/0/day"
    newUpdateTime = GetFileName(filePath)[13:-4]
    if updateTime == newUpdateTime:
        print ("No new rate data")
    else:
        data = urllib2.urlopen(filePath)
        for line in data:
            if CheckString(line):
                arr = line.split()
                time = datetime.strptime(newUpdateTime, '%Y%m%d%H%M')
                ConnectPSQL(arr[0], arr[2], arr[12], arr[3], arr[13], time)
        
        updateTime = newUpdateTime
        data.close()
# FetchRate()
def job_function():
    try:		
        FetchRate()
    except SocketError as e:
        print ("Connection failed, retrying")
        FetchRate()
    except:
        print("Unexpected error, retrying")
        FetchRate()

sched = BlockingScheduler()
sched.add_job(job_function, 'cron', day_of_week='mon-fri', hour="9-16", minute="*/10", timezone="Asia/Taipei")
sched.start()