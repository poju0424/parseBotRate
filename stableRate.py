import requests, os, bs4
import psycopg2
import re
import time
from socket import error as SocketError
import errno
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import logging


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
		# print (lastUpdateTime)
        # print (nowUpdateTime[0].text)
        if nowUpdateTime == lastUpdateTime:
            print ("No new rate data")
        else:
            lastUpdateTime = nowUpdateTime
            rowElem = soup.select('table tbody tr') #per table row
            bankName = "bot"
            cnx = psycopg2.connect("dbname=ddgd2hokh5t1r user=byfozfzreatyuo password=8f54e0b9274e32cefa7c7610ce7b6c4226397338e8cf7bed6892624c97a2c699 host=ec2-54-163-236-33.compute-1.amazonaws.com ")
            cursor = cnx.cursor()
            for i in range(0, len(rowElem), 1):
                colElem = rowElem[i].select('td') #per column in a row
                name = colElem[0].text.replace(" ", "").strip()
                cashBuy = colElem[1].text.replace(" ", "").strip()
                cashSell = colElem[2].text.replace(" ", "").strip()
                rateBuy = colElem[3].text.replace(" ", "").strip()
                rateSell = colElem[4].text.replace(" ", "").strip()
                # nowtime = nowUpdateTime
                # nowtime = datetime.strptime(nowUpdateTime, '%Y-%m-%d %H:%M')
                nowtime = datetime.strptime("".join(nowUpdateTime[0]), '%Y/%m/%d %H:%M')
                currency = re.search('\((...)\)', name)
                tableName = bankName +"_"+ currency.group(1)
                insertDB = ("INSERT INTO "+tableName+"" 
                        "(cashBuy, cashSell, rateBuy, rateSell, datetime) "
                        "VALUES (%s, %s, %s, %s, %s)")
                # data = {
                    # 'cashBuy': cashBuy,
                    # 'cashSell': cashSell,
                    # 'rateBuy': rateBuy,
                    # 'rateSell': rateSell,
                    # 'datetime': nowtime,
                # }
                # cursor.execute(insertDB, data)
                cursor.execute(" INSERT INTO "+tableName+" (cashBuy, cashSell, rateBuy, rateSell, datetime) VALUES (%s, %s, %s, %s, %s) ", (cashBuy, cashSell, rateBuy, rateSell, nowtime))
            print("fetch complete!"+"("+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+")")
            cnx.commit()
            cursor.close()
            cnx.close()
    except SocketError as e:
        # print(e) #prevent server bump
        print ("Connection failed, retrying")
        fetchData()
		
# fetchData() #first time
# schedule.every(5).minutes.do(fetchData)
# while True:
    # schedule.run_pending()
    # time.sleep(60)

sched = BlockingScheduler()
def job_function():
    fetchData()
sched.add_job(job_function, 'cron', day_of_week='mon-fri', hour="9-16", minute="*/5")
sched.start()

