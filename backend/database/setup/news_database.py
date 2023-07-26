import os
import sys

database_path=os.path.join(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(database_path)

import database as db

db.create_table("news",{"date":"DATE","title":"VARCHAR(50)","detail":"TEXT"})
db.insert_data_from_csv("news","news.csv")