import sys
sys.path.append("..")

import database.database as db
import json

json_categorylist=db.get_json_table_data("category")