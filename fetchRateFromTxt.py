import requests, os, bs4
import psycopg2
import urlparse
import re
import time
from socket import error as SocketError
import errno
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import logging

filePath = "http://rate.bot.com.tw/xrt/fltxt/0/day"
f = open(filePath,'r')
lines = f.readline()
f.close()

for line in lines:
    print(line, end='')

#old----------
logging.basicConfig()
lastUpdateTime = 0

def fetchData():
    proxies = {
      'http': 'http://10509070:Qrdcuser88@10.243.17.220:80',
      'https': 'http://10509070:Qrdcuser88@10.243.17.220:80',
    }
    url = 'http://rate.bot.com.tw/xrt?Lang=zh-TW'

    print("Time to fetch~")
    try:
        r = requests.get(url)
        soup = bs4.BeautifulSoup(r.text, "lxml")
        nowUpdateTime = soup.select('.time')
        global lastUpdateTime
        if nowUpdateTime == lastUpdateTime:
            print ("No new rate data")
        else:
            lastUpdateTime = nowUpdateTime
            rowElem = soup.select('table tbody tr') #per table row
            bankName = "bot"
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
            for i in range(0, len(rowElem), 1):
                colElem = rowElem[i].select('td') #per column in a row
                name = colElem[0].text.replace(" ", "").strip()
                cashBuy = colElem[1].text.replace(" ", "").strip()
                cashSell = colElem[2].text.replace(" ", "").strip()
                rateBuy = colElem[3].text.replace(" ", "").strip()
                rateSell = colElem[4].text.replace(" ", "").strip()
                nowtime = datetime.strptime("".join(nowUpdateTime[0]), '%Y/%m/%d %H:%M')
                currency = re.search('\((...)\)', name)
                tableName = bankName +"_"+ currency.group(1)
                cursor.execute(" INSERT INTO "+tableName+" (cashBuy, cashSell, rateBuy, rateSell, datetime) VALUES (%s, %s, %s, %s, %s) ", (cashBuy, cashSell, rateBuy, rateSell, nowtime))
            print("fetch complete!"+"("+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+")")
            cnx.commit()
            cursor.close()
            cnx.close()
    except SocketError as e:
        print ("Connection failed, retrying")
        fetchData()
    except:
        print("Unexpected error, retrying")
        fetchData()

# sched = BlockingScheduler()
# def job_function():
    # fetchData()
# sched.add_job(job_function, 'cron', day_of_week='mon-fri', hour="9-16", minute="*/10", timezone="Asia/Taipei")
# sched.start()

