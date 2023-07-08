import sys
sys.path.append("..")

import database as db

db.create_table("news",{"date":"DATE","title":"VARCHAR(50)","detail":"TEXT"})
db.insert_data_from_csv("news","news.py")