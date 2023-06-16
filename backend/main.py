from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8080"],  # VueアプリケーションのURL
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/HelloWorld")
def read_root():
    return {"Hello":"World"}