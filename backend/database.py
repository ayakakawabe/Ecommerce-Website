import os
import psycopg2
from dotenv import load_dotenv

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

set_DB()

def create_table(table_name:str,col_name_SQLtype:dict[str,str]):
    create_table_key_sql=f"CREATE TABLE {table_name} (id SERIAL PRIMARY KEY"
    column_sql=""
    for col_name,sql_type in col_name_SQLtype.items():
        column_sql+=f",{col_name} {sql_type}"
    sql=create_table_key_sql+column_sql+");"
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

def refer_table(table_name:str):
    with conn:
        with cur:
            cur.execute(f"SELECT * FROM {table_name};")
            result=cur.fetchall()
            for row in result:
                print(row)    

def refer_colmns(table_name:str):
        with conn:
            with cur:
                cur.execute(f"SELECT column_name,data_type,is_nullable FROM information_schema.columns WHERE table_name='{table_name}';")
                results=cur.fetchall()
                for result in results:
                    print("column name:",result[0],"type:",result[1],"null ok:",result[2])


refer_table("news")
#create_table("sample",{"col1":"INT","col2":"TEXT"})
