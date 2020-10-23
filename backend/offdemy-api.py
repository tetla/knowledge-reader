from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json, os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/contents/{page_id}/{content_id}')
async def content(
    page_id: str,
    content_id: str):
    json_path = f"./data/json/{page_id}/{content_id}.json"
    if not os.path.exists(json_path):
        raise HTTPException(status_code=404, detail="Page not found")
    with open(json_path, 'r', encoding='utf-8') as j:
        json_load = json.load(j)
        return json_load

@app.get('/contents/{page_id}')
async def contentslist(
    page_id: str,):
    json_path = f"./data/pagelist/{page_id}.json"
    if not os.path.exists(json_path):
        raise HTTPException(status_code=404, detail="Page not found")
    with open(json_path, 'r', encoding='utf-8') as j:
        json_load = json.load(j)
        return json_load

@app.get('/pagelist')
async def pagelist():
    json_path = "./data/pagelist/all.json"
    with open(json_path, 'r', encoding='utf-8') as j:
        json_load = json.load(j)
        return json_load