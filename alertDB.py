import psycopg2

tableName = ["bot_AUD", "bot_CAD", "bot_CHF", "bot_CNY", "bot_EUR", "bot_GBP", "bot_HKD", "bot_IDR", "bot_JPY", "bot_KRW", "bot_MYR", "bot_NZD", "bot_PHP", "bot_SEK", "bot_SGD", "bot_THB", "bot_USD", "bot_VND", "bot_ZAR"]
# conn = psycopg2.connect("dbname=ddgd2hokh5t1r user=byfozfzreatyuo password=8f54e0b9274e32cefa7c7610ce7b6c4226397338e8cf7bed6892624c97a2c699 host=ec2-54-163-236-33.compute-1.amazonaws.com ")

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

for i in range(0, len(tableName), 1):
    # createTable = "CREATE TABLE IF NOT EXISTS "+tableName[i]+" (ID int NOT NULL, cashBuy varchar NOT NULL, cashSell varchar NOT NULL, rateBuy varchar NOT NULL, rateSell varchar NOT NULL, datetime timestamp NOT NULL);"
    deleteData = "DELETE FROM "+tableName[i]+" WHERE id<95"
    cursor.execute(deleteData)
    # print(i)
conn.commit()