import uvicorn
from fastapi import FastAPI

import real_time_data
import saved_data

app = FastAPI()

@app.get("/realtime/{id}")
async def get_realtime(id):
    return real_time_data.get_data(id)

@app.get("/saved/{id}")
async def get_realtime(id):
    return saved_data.get_data(id)

def start_api():
    uvicorn.run(app, host="127.0.0.1", port=8000)
