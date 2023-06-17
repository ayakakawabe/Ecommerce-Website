import csv
from sqlalchemy import create_engine,text
import os
from dotenv import load_dotenv

load_dotenv()

username=os.getenv("SQL_USERNAME")
password=os.getenv("SQL_PASSWORD")

engine=create_engine(f"postgresql://{username}:{password}@localhost:5432/ivy_sample_database")

with open("./csv_data/news.csv","r",encoding="utf-8") as csvfile:
    reader=csv.reader(csvfile)
    next(reader)
    for row in reader:
        sql=text(f"INSERT INTO news (date,title,detail) VALUES ('{row[0]}','{row[1]}','{row[2]}');")
        with engine.begin() as connection:
            connection.execute(sql)

engine.dispose()