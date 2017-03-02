import requests, os, bs4, time
import mysql.connector
import re
from datetime import date, datetime, timedelta
import schedule
import time
from socket import error as SocketError
import errno
# import pytz

#tz = pytz.timezone('Asia/Taipei')
#lastUpdateTime = datetime.utcnow().replace(tzinfo=pytz.UTC).astimezone(tz).strftime('%Y-%m-%d %H:%M')
lastUpdateTime = 0

def fetchData():
    proxies = {
      'http': 'http://10509070:Qrdcuser88@10.243.17.220:80',
      'https': 'http://10509070:Qrdcuser88@10.243.17.220:80',
    }
    url = 'http://rate.bot.com.tw/xrt?Lang=zh-TW'

    print("Time to fetch~")
    try:
        r = requests.get(url, proxies=proxies)
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
            cnx = mysql.connector.connect(user='jacklee', password='1234',
                                            host='pythonDB',
                                            database='ratedb')
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
                        "VALUES (%(cashBuy)s, %(cashSell)s, %(rateBuy)s, %(rateSell)s, %(datetime)s)")
                data = {
                    'cashBuy': cashBuy,
                    'cashSell': cashSell,
                    'rateBuy': rateBuy,
                    'rateSell': rateSell,
                    'datetime': nowtime,
                }
                cursor.execute(insertDB, data)
            print("fetch complete!"+"("+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+")")
            cnx.commit()
            cursor.close()
            cnx.close()
    except SocketError as e:
        # print(e) #prevent server bump
        print ("Connection failed, retrying")
        fetchData()
		
fetchData() #first time
schedule.every(5).minutes.do(fetchData)
while True:
    schedule.run_pending()
    time.sleep(60)
