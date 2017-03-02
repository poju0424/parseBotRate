#executeQuery("CREATE TABLE IF NOT EXISTS users (sourceName varchar(255), sourceID varchar(255) UNIQUE, sourceType varchar(255) UNIQUE, tick timestamp, linkUser varchar(255), openAutoReply integer NOT NULL, Primary Key (sourceID, sourceType))")
import psycopg2

tableName = ["bot_AUD", "bot_CAD", "bot_CHF", "bot_CNY", "bot_EUR", "bot_GBP", "bot_HKD", "bot_IDR", "bot_JPY", "bot_KRW", "bot_MYR", "bot_NZD", "bot_PHP", "bot_SEK", "bot_SGD", "bot_THB", "bot_USD", "bot_VND", "bot_ZAR"]
conn = psycopg2.connect("dbname=ddgd2hokh5t1r user=byfozfzreatyuo password=8f54e0b9274e32cefa7c7610ce7b6c4226397338e8cf7bed6892624c97a2c699 host=ec2-54-163-236-33.compute-1.amazonaws.com ")
cursor = conn.cursor()

for i in range(0, len(tableName), 1):
    createTable = "CREATE TABLE `"+tableName[i]+"` (`ID` int(11) NOT NULL, `cashBuy` varchar(11) NOT NULL, `cashSell` varchar(11) NOT NULL, `rateBuy` varchar(11) NOT NULL, `rateSell` varchar(11) NOT NULL, `datetime` datetime NOT NULL)"
    cursor.execute(createTable)
    print(i)
	
conn.commit()