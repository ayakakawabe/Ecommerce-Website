import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

username=os.getenv("SQL_USERNAME")
password=os.getenv("SQL_PASSWORD")

conn=psycopg2.connect(
    host="localhost",
    database="ivy_sample_database",
    user=username,
    password=password
)

cur=conn.cursor()

query="SELECT * FROM news;"
cur.execute(query)

result=cur.fetchall()
data=[]
for row in result:
    data.append(row)

cur.close()
conn.close()