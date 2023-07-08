import sys
sys.path.append("..")

import database as db

db.create_table("category",{"title":"VARCHAR(50) NOT NUll","titleJP":"VARCHAR(50) NOT NULL","imgPath":"VARCHAR(50) NOT NULL"})
db.insert_data_from_csv("category","category.csv")
