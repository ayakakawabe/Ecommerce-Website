from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import database.scripts.search_news as news
import database.scripts.search_category as category

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8080"],  # VueアプリケーションのURL
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/NewsList")
def get_all_newslist():
    return news.json_newslist

@app.get("/New_NewsList")
def get_new_newslist():
    return news.json_new_newslist

@app.get("/NewsData/{id}")
async def get_newsdata_by_id(id:int):
    return news.get_json_newsdata_by_id(id)

@app.get("/Category")
def get_categorylist():
    return category.json_categorylist