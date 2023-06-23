import os
import psycopg2
from dotenv import load_dotenv
import csv
import json
import datetime

def set_DB():
    global conn
    global cur
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

def serialize_date(date):
    if isinstance(date,datetime.date):
        return date.isoformat()
    else:
        return date

def get_json_table_data(table_name:str):
    json_col=get_json_columns_data(table_name)
    col_dict=json.loads(json_col)
    table_data={table_name:[]}
    set_DB()
    with conn:
        with cur:
            cur.execute(f"SELECT * FROM {table_name};")
            result=cur.fetchall()
            for row in result:
                d={}
                for i in range(len(col_dict["columns"])):
                    d.update({col_dict["columns"][i]["name"]:serialize_date(row[i])})
                table_data[table_name].append(d)
    json_table_data=json.dumps(table_data,ensure_ascii=False)
    return json_table_data

def get_json_columns_data(table_name:str):
    col_data_dict={"columns":[]}
    set_DB()
    with conn:
        with cur:
            cur.execute(f"SELECT column_name,data_type,is_nullable FROM information_schema.columns WHERE table_name='{table_name}';")
            results=cur.fetchall()
            for result in results:
                d={
                    "name":result[0],
                    "type":result[1],
                    "is_null":result[2]
                    }
                col_data_dict["columns"].append(d)
    col_data_json=json.dumps(col_data_dict)
    return col_data_json

def create_table(table_name:str,col_name_SQLtype:dict[str,str]):
    create_table_key_sql=f"CREATE TABLE {table_name} (id SERIAL PRIMARY KEY"
    column_sql=""
    for col_name,sql_type in col_name_SQLtype.items():
        column_sql+=f",{col_name} {sql_type}"
    sql=create_table_key_sql+column_sql+");"
    set_DB()
    with conn:
        with cur:
            cur.execute(sql)
            cur.execute(f"SELECT column_name,data_type,is_nullable FROM information_schema.columns WHERE table_name='{table_name}';")
            results=cur.fetchall()
            for result in results:
                print("column name:",result[0],"type:",result[1],"null ok:",result[2])
            y_n=input("database commit? y/n:")
            if(y_n=="y"):
                conn.commit()
            else:
                conn.rollback()

def insert_data_from_csv(table_name:str,csv_file_name:str):
    csv_path=os.path.join("backend\\csv_data\\",csv_file_name)
    with open(csv_path,"r",encoding="utf-8-sig") as csvfile:
        reader=csv.reader(csvfile)
        header=next(reader)
        col_data_all=json.loads(get_json_columns_data(table_name))
        col_data=[col_data_all["columns"][i]["name"] for i in range(len(col_data_all["columns"]))]
        if col_data[1:len(col_data)]==header:
            set_DB()
            with conn:
                with cur:
                    for row in reader:
                        sql=f"INSERT INTO {table_name} ("
                        for col in header[0:len(header)-1]:
                            sql+=f"{col},"
                        sql+=f"{header[len(header)-1]})"
                        sql+=f" VALUES ('{row[0]}','{row[1]}','{row[2]}');"
                        cur.execute(sql)
                    cur.execute("SELECT * FROM news;")
                    result=cur.fetchall()
                    for row in result:
                        print(row)
                    y_n=input("database commit? y/n:")
                    if(y_n=="y"):
                        conn.commit()
                    else:
                        conn.rollback()
                        cur.execute(f"SELECT MAX({col_data[0]}) FROM {table_name};")
                        max_serial_value=cur.fetchone()[0]
                        new_serial_value=max_serial_value+1
                        cur.execute(f"ALTER SEQUENCE {table_name}_{col_data[0]}_seq RESTART WITH {new_serial_value};")
                        conn.commit()

#insert_data_from_csv("news","news.csv")
#print(get_json_table_data("news"))
#print(get_json_columns_data("news"))
#create_table("sample",{"col1":"INT","col2":"TEXT"})
