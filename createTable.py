#executeQuery("CREATE TABLE IF NOT EXISTS users (sourceName varchar(255), sourceID varchar(255) UNIQUE, sourceType varchar(255) UNIQUE, tick timestamp, linkUser varchar(255), openAutoReply integer NOT NULL, Primary Key (sourceID, sourceType))")
import psycopg2

#cnx = mysql.connector.connect(user='byfozfzreatyuo', password='8f54e0b9274e32cefa7c7610ce7b6c4226397338e8cf7bed6892624c97a2c699',host='ec2-54-163-236-33.compute-1.amazonaws.com',database='ddgd2hokh5t1r')
conn = psycopg2.connect("dbname=ddgd2hokh5t1r user=byfozfzreatyuo password=8f54e0b9274e32cefa7c7610ce7b6c4226397338e8cf7bed6892624c97a2c699 host=ec2-54-163-236-33.compute-1.amazonaws.com ")
cursor = conn.cursor()
# insertDB = ("CREATE TABLE IF NOT EXISTS users (sourceName varchar(255), sourceID varchar(255) UNIQUE, sourceType varchar(255) UNIQUE, tick timestamp, linkUser varchar(255), openAutoReply integer NOT NULL, Primary Key (sourceID, sourceType))")
# cursor.execute(insertDB)
cursor.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
conn.commit()