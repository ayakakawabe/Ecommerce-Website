import database.database as db
import json

json_newslist=db.get_json_table_data("news")
newslist=json.loads(json_newslist)["news"]
print(newslist)

def get_json_newsdata_by_id(search_id):
    for newsdata in newslist:
        if "id" in newsdata and newsdata["id"]==search_id:
            return json.dumps(newsdata,ensure_ascii=False)


new_newslist=newslist[len(newslist)-2:len(newslist)]
json_new_newslist=json.dumps(new_newslist,ensure_ascii=False)
