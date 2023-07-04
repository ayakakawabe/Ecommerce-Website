import csv
import os
import psycopg2
from dotenv import load_dotenv

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

create_table_sql="""
CREATE TABLE news (
id SERIAL PRIMARY KEY,
date DATE,
title VARCHAR(50),
detail TEXT
);
"""
cur.execute(create_table_sql)

with open("./csv_data/news.csv","r",encoding="utf-8") as csvfile:
    reader=csv.reader(csvfile)
    next(reader)
    for row in reader:
        insert_sql=f"INSERT INTO news (date,title,detail) VALUES ('{row[0]}','{row[1]}','{row[2]}');"
        cur.execute(insert_sql)

cur.execute("SELECT * FROM news;")
result=cur.fetchall()
for row in result:
    print(result)

conn.commit()

cur.close()
conn.close()