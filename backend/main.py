from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import treat_news_data;

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8080"],  # VueアプリケーションのURL
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/NewsData")
def read_root():
    return treat_news_data.data